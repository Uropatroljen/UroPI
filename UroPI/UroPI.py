import os
from Server import c_Server
from NetworkUtils import c_NetworkUtils
from ConfigManager import c_ConfigManager

class c_UroPI:
    configManager : c_ConfigManager

    def __init__(self) -> None:
        self.configManager = c_ConfigManager()
        self.Main()

#This is or main file.
#This file should be launched when attempting to turn on the program.    
    def Main(self):
        #Setup class with pass
        NetUtils = c_NetworkUtils(self.configManager)
        #Check if wifi is connect
        if NetUtils.IsConnected() is False : 
            #if not wifi connected create config
            NetUtils.CreateWifiConfig()
            #reboot device after changes
            self.Reboot()
        #start server parse in the config file
        server = c_Server(self.configManager)

    def Reboot(self):
        os.system('reboot')        

c_UroPI()