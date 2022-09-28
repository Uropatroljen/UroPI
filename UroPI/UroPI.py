import os
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
        #Setup class with pass
        self.__NetUtils = c_NetworkUtils(self.__configManager)
        #Check if wifi is connect
        if self.__NetUtils.IsConnected() is False : 
            #if not wifi connected create config
            self.__NetUtils.CreateWifiConfig()
            #reboot device after changes
            self.__Reboot()
        #start server parse in the config file
        server = c_Server(self.__configManager)

    def __Reboot(self):
        os.system('reboot')        

c_UroPI()