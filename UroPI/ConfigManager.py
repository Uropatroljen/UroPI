import configparser
from operator import truediv


class c_ConfigManager:
    
    __config : configparser.ConfigParser 
        
    def __init__(self):
        #Set attribute of configparser
        self.__config = configparser.ConfigParser()
        #Read the configuration file
        self.__config.read("configurations.ini")

    def __SaveConfig(self):
        """Save the configurationFile"""
        try:
            with open(r"configurations.ini", 'w') as configfileObj:
                self.__config.write(configfileObj)
                configfileObj.flush()
                configfileObj.close()
                print("Config file 'configurations.ini' created")
        except:
            return None    
    
    def IsHotspotEnabled(self) -> bool :
        """Return wifi or hotspot due to the settings in init"""
        try:
            return eval(self.__config["networkOptions"]["hotspot"])
        except:
            return None
    def IsWifiEnabled(self) -> bool :
        """Return wifi or hotspot due to the settings in init"""
        try:
            return eval(self.__config["networkOptions"]["wifi"])
        except:
            return None   

    def GetIp(self) -> str :
        """Get the ip from configuration file."""
        try:
            self.__config.set
            return self.__config["uroSettings"]["serverAddress"]
        except:
            return None    
    def GetSsid(self) -> str : 
        """Get ssid from netwrok settings"""
        try:
            return self.__config["networkOptions"]["ssid"]
        except:
            return None

    def GetPsk(self) -> str : 
        """Get ssid from netwrok settings"""
        try:
            return self.__config["networkOptions"]["psk"]
        except:
            return None
    
    def GetWifiSetup(self) -> tuple :
        """Get ssid and psk for network"""
        try:
            tup = (self.__config["networkOptions"]["ssid"], self.__config["networkOptions"]["psk"])
            return tup
        except:
            return None
    def SetupNetwork(self, ssid : str, psk : int):
        """Setup network configuration files"""
        try:
            self.__config["networkOptions"]["ssid"]= ssid
            self.__config["networkOptions"]["psk"] = psk
            self.__SaveConfig()
        except:
            return None

    def SetIp(self, ip : str):
        """overwrite ipaddress in configuration file"""
        try:
            #Set the serverAddress value to given value
            self.__config["uroSettings"]["serverAddress"] = ip
            #writing changes to configuration file, so next reboot contain new ip.
            self.__SaveConfig()
            return True
        except:
            return False
    def SetNetworkConnection(self, num : int, enable : bool):
        """0 hotspot, 1 wifi, set the startup configuration 0 = hotspot,  enable = true/false """
        try:
            if num is 0:
                self.__config["networkOptions"]["wifi"] = str(not enable)
                self.__config["networkOptions"]["hotspot"] = str(enable)
                self.__SaveConfig()
            elif num is 1:
                self.__config["networkOptions"]["hotspot"] = str(not enable)
                self.__config["networkOptions"]["wifi"] = str(enable)
                self.__SaveConfig()
            
            return True
        except:
            return None

    def GetPort(self) -> str:
        try:
            """Get port from configuration file as str"""
            return int(self.__config["uroSettings"]["Port"])
        except:
            return None        