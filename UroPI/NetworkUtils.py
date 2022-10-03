
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
        
    #Method for creating wifi configuration file
    # def CreateWifiConfig(self):
    #     #setting up file contents
    #     config_lines = [
    #         'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev',
    #         'update_config=1',
    #         'country=DK',
    #         '\n',
    #         'network={',
    #         '\tssid=\"' + self.configParse.config["NetworkOptions"]["ssid"] + "\"",
    #         '\tpsk=\"'+ self.configParse.config["NetworkOptions"]["psk"] + "\"",
    #         '}'
    #         ]
    #     config = '\n'.join(config_lines)
    #     #display additions
    #     print(config)
    #     #give access and writing. may have to do this manually beforehand
    #     os.popen("sudo chmod a+w /etc/wpa_supplicant/wpa_supplicant.conf")
    #     #writing to file
    #     with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as wifi:
    #         wifi.write(config)
    #     #displaying success
    #     print("wifi config added")
 
    def ConnectToWifi(self):
        """By terminal connect to wifi with configuration files"""
        #connecting to wifi
        os.system("nmcli device wifi connect\""+self.__configMan.GetSsid+"\" password \""+self.__configMan.GetPsk+"\"")
        #sleeping before getting our ipv4 address
        sleep(2000)
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
        os.system("sudo systemctl enable hostapd dnsmasq")
        os.system("cat /etc/dhcpcd.conf.hotspot | sudo tee a /etc/dhcpcd.conf >/dev/null")
        os.system("cat /etc/dnsmasq.conf.hotspot | sudo tee a /etc/dnsmasq.conf >/dev/null")
        os.system("sudo service hostapd restart")
        os.system("sudo service dnsmasq restart")
        self.__configMan.SetNetworkConnection(0, True)
        os.system("sudo reboot")

    def DisableHotspot(self):
        """disable hotspot and set the original config files"""
        os.system("sudo systemctl disable hostapd dnsmasq")
        os.system("cat /etc/dhcpcd.conf.wifi | sudo tee a /etc/dhcpcd.conf >/dev/null")
        os.system("cat /etc/dnsmasq.conf.wifi | sudo tee a /etc/dnsmasq.conf >/dev/null")
        os.system("sudo service hostapd stop")
        os.system("sudo service dnsmasq stop")
        self.__configMan.SetNetworkConnection(1, True)
        os.system("sudo reboot")
      
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