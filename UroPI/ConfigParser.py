import configparser
from distutils.command.config import config

class c_ConfigParser:
    
    config : configparser    
        
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("configurations.ini")

     
        
       
    def GetIp(self):
        ip = self.config["UroSettings"]["ConnectionString"]
        return ip
    
    def GetPort(self):
        port = int(self.config["UroSettings"]["Port"])
        return port