'''
Created on Jul 5, 2009

@author: cthos <daginus@gmail.com>
'''

from engine.flare import Flare

class EssencePool:
    '''
    classdocs
    '''
    personal = 0
    peripheral = 0
    
    maxPeripheral = 0
    maxPersonal = 0
    
    flareObj = ""
    
    recoveryRates = {"active":0, "lRest":0, "sleep": 0}
    
    hearthstones = []
    committedEssence = []

    def __init__(self, recoveryRate, exType = "solar"):
        '''
        Constructor
        '''
        exType = exType.lower()

        self.setRecoveryRates(recoveryRate)
        self.flareObj = Flare(exType)
        
    def useEssence(self, pool, amount):
        if pool == "personal":
            if amount > self.personal:
                raise Exception("Not enough Personal Essence")
            self.personal -= amount
        elif pool == "peripheral":
            if amount > self.peripheral:
                raise Exception("Not enough Peripheral Essence")
            self.peripheral -= amount
                        
    def setMaxes(self, personal, peri):
        self.maxPeripheral = peri
        self.maxPersonal = personal
        self.peripheral = self.maxPeripheral
        self.personal = self.maxPersonal       
    
    def resetEssencePool(self):
        self.personal = self.maxPersonal
        self.peripheral = self.maxPeripheral
    
    def recoverWithRest(self, hours, type = "active"):
        if not self.recoveryRates.has_key(type):
            return False
        self.regenEssence(hours * self.recoveryRates[type])
        
    def recoverWithStunt(self, numDie):
        self.regenEssence(numDie * 2)
    
    def regenEssence(self, amt):
        self.peripheral += amt
        
        if self.peripheral > self.maxPeripheral:
            self.personal += self.peripheral - self.maxPeripheral
            self.peripheral = self.maxPeripheral
            
        if self.personal > self.maxPersonal:
            self.personal = self.maxPersonal
    
    def checkFlareLevel(self):
        amtUsed = self.maxPeripheral - self.peripheral
        
        return self.flareObj.getFlareMessage(amtUsed)
    
    def setRecoveryRates(self, normalRate):
        self.recoveryRates = {"active":normalRate, "lRest":normalRate + 4, "sleep": normalRate + 8}
    