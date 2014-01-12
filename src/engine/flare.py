'''
Created on Aug 2, 2009

@author: cthos
'''

class Flare():
    '''
    classdocs
    '''
    exType = ""


    def __init__(self, exaltType = "solar"):
        '''
        Constructor
        '''
        self.exType = exaltType
        
    def getFlareMessage(self, peripheralEssenceSpent):
        if self.exType == 'solar':
            return self.getSolarMessage(peripheralEssenceSpent)
        elif self.exType == 'lunar':
            return self.getLunarMessage(peripheralEssenceSpent)
        
    def getSolarMessage(self, peripheralEssenceSpent):
        return "Not yet implemented"
    
    def getLunarMessage(self, peripheralEssenceSpent):
        if peripheralEssenceSpent == 0:
            return ""
        elif peripheralEssenceSpent <= 3:
            return "Caste mark glitters and is visible from certain angles, " +\
            "and Tell becomes Prominent"
        elif peripheralEssenceSpent <= 7:
            return "Caste mark and tattoos burn and shine through anything " +\
            "placed over them. Tell is impossible to miss. Stealth at +2 difficulty"
        elif peripheralEssenceSpent <= 10:
            return "Radiating coruscant, blue-silver aura bright enough to read by " +\
            "and the character is now forced into true forms."
        elif peripheralEssenceSpent <= 15:
            return "Locked into true forms, and engulfed in a bonfire of Essence. " +\
            "Objects that come into contact with the aura may become damp and warped, " +\
            "as if they had been exposed to the night and the elements for many days."
        elif peripheralEssenceSpent >= 16:
            return "The character is surmounted by a coldly burning totemic image. " +\
            "Still locked into true shapes."
            
        return "Not found!"
        