import os
from sqlite3 import connect
from Server import c_Server
from NetworkUtils import c_NetworkUtils
from ConfigManager import c_ConfigManager

class c_UroPI:
    __configManager : c_ConfigManager
    __NetUtils : c_NetworkUtils
    
    def __init__(self) -> None:
        self.__configManager = c_ConfigManager()
        self.Main()

#This is or main file.
#This file should be launched when attempting to turn on the program.    
    def Main(self):
        #Setup network utils parsing config manager.
        self.__NetUtils = c_NetworkUtils(self.__configManager)
        #Get Network setup
        networkOptions = self.__configManager.GetNetworkOptions()
        #If network ssid and psk is not set, start hotspot.
        if networkOptions[0] == "" and networkOptions[1] == "" :
            self.__NetUtils.StartHostpot() 
        #else connect to wifi
        elif self.__NetUtils.ConnectToWifi is None :
            self.__Reboot
            
        server = c_Server(self.__configManager)

    def __Reboot(self):
        os.system('reboot')        

c_UroPI()