from time import sleep
import unittest
from NetworkUtils import c_NetworkUtils
from ConfigManager import c_ConfigManager
from Generate_Config import c_Generate_Config

class Unit_Test(unittest.TestCase):
    config : c_ConfigManager    
    network : c_NetworkUtils

    def test_GenerateConfigFile(self):
       #creating a try catch for error handling.
        try:
            #resseting configuration file
            configGenerater = c_Generate_Config()
            result = configGenerater.CreateConfig()
            #check if configuration file did resset.
            self.assertIs(result, True)
        except:
            self.assertIs(result, False)

    def test_GetIP(self):
        #creating object of config manager
        self.config = c_ConfigManager()
        #creating a object og network utils and parseing configmanager
        self.network = c_NetworkUtils(self.config)
        #Getting ipv4 address. 
        ip = self.network.get_ip_address()
        #setting up ip in cofiguration file
        result = self.config.SetIp(ip)
        #check if we get and true result.
        self.assertIs(result, True)

    def test_StandardConfigfile(self):
        #creating object of configmanager
        self.config = c_ConfigManager()
        #resseting config file
        c_Generate_Config().CreateConfig()
        #sleeping 2 sec 
        sleep(2)
        #creating a result to check if it works
        res : bool = False 
        try :
            #getting ip
            ip = self.config.GetIp() 
            #getting port
            port = self.config.GetPort()
            #check if port and ip is what we expected
            if ip == '192.168.4.1' and port == 1883:
                res = True
            else:
                res = False
        except:
            res = False
        #check if res is changed to true
        self.assertIs(res, True)

    def test_WifiConfigFile(self) :
        #creating object of config manager
        self.config = c_ConfigManager()
        #creating return result
        res : bool = False
        try:
            #writing network settings in configuration file
            self.config.SetupNetwork("Ukendt", "Kode1234!")
            #getting password
            psk = self.config.GetPsk()
            #getting ssid
            ssid = self.config.GetSsid() 
            #checking if ssid and psk is set
            if ssid == "Ukendt" and psk == "Kode1234!" :
                res = True
            else : 
                res = False 
        except:
            res = False
            #check result
        self.assertIs(res, True)


