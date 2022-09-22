import configparser


class c_ConfigManager:
    
    config : configparser    
        
    def __init__(self):
        #Set attribute of configparser
        self.config = configparser.ConfigParser()
        #Read the configuration file
        self.config.read("configurations.ini")

    def GetIp(self) -> str :
        """Get the ip from configuration file."""
        return self.config["UroSettings"]["ConnectionString"]
      
    
    def SetIp(self, ip : str):
        """overwrite ipaddress in configuration file"""
        #Set the connectionString value to given value
        self.config.ConfigParser.set("UroSettings", "ConnectionString", ip)
        #writing changes to configuration file, so next reboot contain new ip.
        with open(r"configurations.ini", 'w') as configfileObj:
            self.config.ConfigParser.write(configfileObj)
            configfileObj.flush()
            configfileObj.close()
            print("Config file 'configurations.ini' created")
    
    def GetPort(self) -> str:
        """Get port from configuration file as str"""
        return int(self.config["UroSettings"]["Port"])
        