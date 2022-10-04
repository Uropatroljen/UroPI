import os
from sqlite3 import connect
from Server import c_Server
from NetworkUtils import c_NetworkUtils
from ConfigManager import c_ConfigManager
from Generate_Config import c_Generate_Config

class c_UroPI:
    __configManager : c_ConfigManager
    __NetUtils : c_NetworkUtils
    state = True
    def __init__(self) -> None:
        self.__configManager = c_ConfigManager()
        self.Main()

#This is or main file.
#This file should be launched when attempting to turn on the program.    
    def Main(self):
        if(self.state == False):
            #Setup network utils parsing config manager.
            self.__NetUtils = c_NetworkUtils(self.__configManager)
            hotspot = self.__configManager.IsHotspotEnabled()
            wifi = self.__configManager.IsWifiEnabled()

            #if hotspot and wifi is False, start up hotspot configuration.
            if hotspot and wifi == False : 
                self.__NetUtils.StartHostpot()
            # if hotspot is false and wifi is true run wifi setup
            elif hotspot == False and wifi == True:
                #Get tuple of wifi configuration index 0 ip, index 1 psw
                wifiSetup = self.__configManager.GetWifiSetup()
                if wifiSetup is None:
                    self.__NetUtils.StartHostpot()
                #check if both is str
                if wifiSetup[0] and wifiSetup[1] is str:
                    #connect to wifi 
                    if self.__NetUtils.ConnectToWifi() is None :
                        self.__Reboot()

            if self.__configManager.GetIp() is None :
                c_Generate_Config().CreateConfig()
                self.__Reboot()
            else :
                server = c_Server(self.__configManager)
    server = c_Server('0.0.0.0',1883)
        

            

    def __Reboot(self):
        os.system('reboot')        

c_UroPI()