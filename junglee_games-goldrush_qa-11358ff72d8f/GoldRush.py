from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.core.android import *

#Modules
import Game.Config as GameConfig
import Game.Constants as GameConstants
import Modules.DEX as GameUtils

#Prepare For Test Execution
class PrepareForExecution:
    try :
        android.check_app(GameConfig.PACKAGE_NAME)               
        if GameConfig.REINSTALL:
            GameUtils.InstallBuild(True)
    except :
        GameUtils.InstallBuild()    
    start_app(GameConfig.PACKAGE_NAME)
    gameLaunched = False
    while gameLaunched == False:
        try :        
            poco = UnityPoco()
            poco(GameConstants.GAME_MANAGER).wait_for_appearance()
            gameLaunched = True
        except :        
            sleep(1)

#Import Test Cases
import TestCases.DealCards

#Execute Test Cases

auto_setup(__file__)