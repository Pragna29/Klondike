#Imports 
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.core.android import *

#Modules
import Game.Config as GameConfig
import Game.Constants as GameConstants
import Modules.DEX as GameUtils

#Initializations
android = Android()        
poco = UnityPoco()

#Data

#Execution
klondikeBoard = GameUtils.GetKlondikeBoard()

for slot in range(len(klondikeBoard.stack1)):
    if len(klondikeBoard.stack1[slot].children()) > 0:
        klondikeBoard.stack1[slot][0].drag_to(poco(GameConstants.FOUNDATION_DIAMONDS))

for slot in range(len(klondikeBoard.stack2)):
    if len(klondikeBoard.stack2[slot].children()) > 0:
        klondikeBoard.stack2[slot][0].drag_to(poco(GameConstants.FOUNDATION_DIAMONDS))

for slot in range(len(klondikeBoard.stack3)):
    if len(klondikeBoard.stack3[slot].children()) > 0:
        klondikeBoard.stack3[slot][0].drag_to(poco(GameConstants.FOUNDATION_DIAMONDS))
        
for slot in range(len(klondikeBoard.stack4)):
    if len(klondikeBoard.stack4[slot].children()) > 0:
        klondikeBoard.stack4[slot][0].drag_to(poco(GameConstants.FOUNDATION_DIAMONDS))
        
for slot in range(len(klondikeBoard.stack5)):
    if len(klondikeBoard.stack5[slot].children()) > 0:
        klondikeBoard.stack5[slot][0].drag_to(poco(GameConstants.FOUNDATION_DIAMONDS))
        
for slot in range(len(klondikeBoard.stack6)):
    if len(klondikeBoard.stack6[slot].children()) > 0:
        klondikeBoard.stack6[slot][0].drag_to(poco(GameConstants.FOUNDATION_DIAMONDS))
        
for slot in range(len(klondikeBoard.stack7)):
    if len(klondikeBoard.stack7[slot].children()) > 0:
        klondikeBoard.stack7[slot][0].drag_to(poco(GameConstants.FOUNDATION_DIAMONDS))
        
auto_setup(__file__)    