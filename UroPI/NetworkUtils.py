
import os
import socket
from time import sleep

from ConfigManager import c_ConfigManager

class c_NetworkUtils :
    #attribute for connection fails 
    __connectionFails = 0
    #Object of configManager
    __configMan : c_ConfigManager
    #constructor with c_ConfigManager as paramater
    def __init__(self, configReader : c_ConfigManager):
        self.__configMan = configReader
    
    def ConnectToWifi(self):
        """By terminal connect to wifi with configuration files"""
        #connecting to wifi
        os.system("nmcli device wifi connect\""+self.__configMan.GetSsid+"\" password \""+self.__configMan.GetPsk+"\"")
        #sleeping before getting our ipv4 address
        sleep(2)
        if(self.__connectionFails >= 10):
            return None
        #check if we got an ipv4 address
        if self.get_ip_address() is str :
            return self.get_ip_address()
        #try to reconnect if not
        else:
            self.__connectionFails += 1
            self.ConnectToWifi()
            print("Retrying to connect to wifi")
    
    def StartHostpot(self):
        """Set up the hotspot configuration files and rebooting systemctl"""
        if self.__configMan.GetSsid() is not None:
            os.system(f"nmcli con down id \"{self.__configMan.GetSsid()}\"")
        os.system("nmcli con up hoturo")
        self.__configMan.SetNetworkConnection(0, True)
        
    def DisableHotspot(self):
        """disable hotspot and set the original config files"""
        os.system("nmcli con down hoturo")
        self.__configMan.SetNetworkConnection(1, True)
      
    def get_ip_address(self) -> str:
        """Get ip address from INET (IPV4)"""
        #Af_Inet represent the address & protocol families.
        #SOCK_DGRAM connectionless, unreliable datagrams(udp)
        #Create a socket with internet protocol version 4 (ipv4) using DGRAM
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #connect to google dns on port 80
        #Set the config ip address to the bound socket.
        sock.connect(("8.8.8.8", 80))
        #getsockname returns the current address bound to the socket
        #Check if the bound socket is set 
        if sock.getsockname()[0] is not None :
            try :
                #returning the ip Address
                return sock.getsockname()[0]
            except error as error:
                print(error)
                return None
        else :
         return None