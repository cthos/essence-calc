import os, ConfigParser

class StoredCharacter:
    configLoc = '~/.essence_calc/'

    """
    Holds a representation of a stored character,
    """
    def __init__(self, characterName, options):
        self.characterName = characterName
        pass

    @staticmethod
    def load(characterName):
        config_file = StoredCharacter.getConfigFileLoc(characterName)

        if not os.path.exsists(config_file):
            return False

        config = ConfigParser.ConfigParser()
        config.read(config_file)

    def save(self):
        config_file = StoredCharacter.getConfigFileLoc(self.characterName)

        config = ConfigParser.ConfigParser()

        if not os.path.exists(config_file):
            config.add_section('character')
            config.set('prefs', 'alert_level', "30")

            with open(config_file, 'wb') as configfile:
                config.write(configfile)
        else:
            config.read(config_file)

        self.options = config

    @staticmethod
    def getConfigFileLoc(characterName):
        """
        Loads a config file from the standard config dir.
        """
        config_loc = os.path.expanduser(StoredCharacter.configLoc)

        if not os.path.exists(config_loc):
            os.mkdir(config_loc)

        config_file = config_loc + characterName + '.cnf'

        return config_file