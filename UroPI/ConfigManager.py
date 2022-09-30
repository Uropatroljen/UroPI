import configparser


class c_ConfigManager:
    
    __config : configparser    
        
    def __init__(self):
        #Set attribute of configparser
        self.__config = configparser.ConfigParser()
        #Read the configuration file
        self.__config.read("configurations.ini")

    def __SaveConfig(self):
          with open(r"configurations.ini", 'w') as configfileObj:
            self.__config.ConfigParser.write(configfileObj)
            configfileObj.flush()
            configfileObj.close()
            print("Config file 'configurations.ini' created")
        

    def GetIp(self) -> str :
        """Get the ip from configuration file."""
        return self.__config["uroSettings"]["serverAddress"]
    
    def GetSsid(self) -> str : 
        """Get ssid from netwrok settings"""
        return self.__config["networkOptions"]["ssid"]
    
    def GetPsk(self) -> str : 
        """Get ssid from netwrok settings"""
        return self.__config["networkOptions"]["psk"]
    
    def GetNetworkOptions(self) -> tuple :
        """Get ssid and psk for network"""
        tup = (self.__config["networkOptions"]["ssid"], self.__config["networkOptions"]["psk"])
        return tup
  
    def SetupNetwork(self, ssid : str, psk : int):
        """Setup network configuration files"""
        self.__config.ConfigParser.set("networkOptions", "ssid", ssid)
        self.__config.ConfigParser.set("networkOptions", "psk", psk)
        self.__SaveConfig()
        
    def SetIp(self, ip : str):
        """overwrite ipaddress in configuration file"""
        #Set the serverAddress value to given value
        self.__config.ConfigParser.set("uroSettings", "serverAddress", ip)
        #writing changes to configuration file, so next reboot contain new ip.
        self.__SaveConfig(self)
    
    def GetPort(self) -> str:
        """Get port from configuration file as str"""
        return int(self.__config["uroSettings"]["Port"])
        