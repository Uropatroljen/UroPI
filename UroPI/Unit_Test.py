import imp
from operator import truediv
import re
from time import sleep
import unittest
from NetworkUtils import c_NetworkUtils
from ConfigManager import c_ConfigManager
from Generate_Config import c_Generate_Config

class Unit_Test(unittest.TestCase):
    config : c_ConfigManager    
    network : c_NetworkUtils

    def test_GenerateConfigFile(self):
        try:
            configGenerater = c_Generate_Config()
            result = configGenerater.CreateConfig()
            self.assertIs(result, True)
        except:
            self.assertIs(result, False)

    def test_GetIP(self):
        self.config = c_ConfigManager()
        self.network = c_NetworkUtils(self.config)
        ip = self.network.get_ip_address()
        result = self.config.SetIp(ip)
        self.assertIs(result, True)

    def test_StandardConfigfile(self):
        self.config = c_ConfigManager()
        c_Generate_Config().CreateConfig()
        sleep(1)
        res : bool = False 
        try :
            ip = self.config.GetIp() 
            port = self.config.GetPort()
            if ip == '192.168.4.1' and port == 1883:
                res = True
            else:
                res = False
        except:
            res = False
        self.assertIs(res, True)

    def test_WifiConfigFile(self) :
        self.config = c_ConfigManager()
        res : bool = False
        try:
            self.config.SetupNetwork("Kalk24", "Kode2489!")
            psk = self.config.GetPsk()
            ssid = self.config.GetSsid() 
            if ssid == "Kalk24" and psk == "Kode2489!" :
                res = True
            else : 
                res = False 
        except:
            res = False
        self.assertIs(res, True)


