'''
Created on Jul 5, 2009

@author: cthos
'''
import sys
from engine.essence import *

perPool = raw_input("What is your personal Essence Pool? ")
periPool = raw_input("What is your peripheral Essence Pool? ")

exaltType = raw_input("What kind of exalt are you (Solar, Lunar, Abyssal, Infernal, Dragon-Blooded)? ")

essPool = EssencePool(5, exaltType)
essPool.setMaxes(int(perPool), int(periPool))

while True:
    print "Your Current Pool is: \033[94m%s personal\x1B[m and \033[92m%s peripheral\x1B[m" % (essPool.personal, essPool.peripheral)
    print ""
    essEx = raw_input("Enter essence expenditure: ")
    
    if essEx == 'quit':
        break
    
    if essEx == "recover":
        hours = raw_input("How many hours? ")
        essPool.recoverWithRest(int(hours))
        continue
    if essEx == "stunt":
        die = raw_input("How many die? ")
        essPool.recoverWithStunt(int(die))
        continue
    
    if essEx == 'reset':
        essPool.resetEssencePool()
        continue
    
    tehPools = raw_input("From which pool? 1 for personal, 2 for peripheral: ")
    pool = ''
    
    if int(tehPools) == 1:
        pool = "personal"
    else:
        pool = "peripheral"
    
    try:
        essPool.useEssence(pool, int(essEx))
    except Exception as e:
        print str(e)
        continue
    
    flare = essPool.checkFlareLevel()
    
    if flare:
        print "\033[93mWARNING: You are now flaring. Message: %s\x1B[m" % flare
        
    print ""