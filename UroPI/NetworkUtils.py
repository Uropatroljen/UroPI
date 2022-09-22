import os
import subprocess
import socket

from ConfigManager import c_ConfigManager

class c_NetworkUtils :
    
    #Object of configManager
    configReader : c_ConfigManager
    #constructor with c_ConfigManager as paramater
    def __init__(self, configReader : c_ConfigManager):
        self.configReader = configReader
        
    #Method for creating wifi configuration file
    def CreateWifiConfig(self):
        #setting up file contents
        config_lines = [
            'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev',
            'update_config=1',
            'country=DK',
            '\n',
            'network={',
            '\tssid=\"' + self.configParse.config["NetworkOptions"]["ssid"] + "\"",
            '\tpsk=\"'+ self.configParse.config["NetworkOptions"]["psk"] + "\"",
            '}'
            ]
        config = '\n'.join(config_lines)
        #display additions
        print(config)
        #give access and writing. may have to do this manually beforehand
        os.popen("sudo chmod a+w /etc/wpa_supplicant/wpa_supplicant.conf")
        #writing to file
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as wifi:
            wifi.write(config)
        #displaying success
        print("wifi config added")
    #TODO
    def IsConnected(self):
        try:
            proc = subprocess.check_output(['sudo', 'iwgetid']).decode()
        except :
            return False
        
    def get_ip_address(self) -> str:
        """Get ip address from INET (IPV4)"""
        #Af_Inet represent the address & protocol families.
        #SOCK_DGRAM connectionless, unreliable datagrams(udp)
        #Create a socket with internet protocol version 4 (ipv4) using DGRAM
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #connect to google dns on port 80
        sock.connect(("8.8.8.8", 80))
        #getsockname returns the current address bound to the socket
        #Check if the bound socket is set 
        if sock.getsockname()[0] is not None :
            #Set the config ip address to the bound socket.
            self.configReader.SetIp(sock.getsockname()[0])
            #returning the ip Address
        return sock.getsockname()[0]    