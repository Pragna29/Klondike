from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.core.android import *

#Modules
import Game.Config as GameConfig
import Game.Constants as GameConstants

#Initializations
android = Android()        
poco = UnityPoco()

#Classes
class GetKlondikeBoard():
    def __init__(self):          
        poco = UnityPoco()
        tableau = poco(GameConstants.TABLEAU).children()
        for stack in range(len(tableau)):
            if stack == 0:
                self.stack1 = tableau[stack].children()
            if stack == 1:
                self.stack2 = tableau[stack].children()
            if stack == 2:
                self.stack3 = tableau[stack].children()
            if stack == 3:
                self.stack4 = tableau[stack].children()
            if stack == 4:
                self.stack5 = tableau[stack].children()
            if stack == 5:
                self.stack6 = tableau[stack].children()
            if stack == 6:
                self.stack7 = tableau[stack].children()                
        self.tableau = tableau
        
#Definations
def InstallBuild(clean = False):
    if clean :
        uninstall(GameConfig.PACKAGE_NAME)        

    if GameConfig.PRODUCTION_GAME_ENVIORNMENT:
        install(GameConfig.PRODUCTION_BUILD_PATH)        
    else:
        install(GameConfig.DEVELOPMENT_BUILD_PATH) 

auto_setup(__file__)