import configparser

class c_Generate_Config():

    config_file : configparser.ConfigParser

    def __init__(self) -> None:
        # CREATE OBJECT
        self.config_file = configparser.ConfigParser()
        
    def CreateConfig(self):
        try:
            # ADD SECTION
            self.config_file.add_section("uroSettings")
            self.config_file.add_section("networkOptions")
            # ADD SETTINGS TO SECTION
            self.config_file.set("uroSettings", "serverAddress", "192.168.4.1")
            self.config_file.set("uroSettings", "port", "1883")

            self.config_file.set("networkOptions", "wifi", "False")
            self.config_file.set("networkOptions", "hotspot", "False")
            self.config_file.set("networkOptions", "ssid", "")
            self.config_file.set("networkOptions", "psk", "")

            with open(r"UroPI\configurations.ini", 'w') as configfileObj:
                self.config_file.write(configfileObj)
                configfileObj.flush()
                configfileObj.close()
            print("Config file 'configurations.ini' created")
            # PRINT FILE CONTENT
            read_file = open("UroPI\configurations.ini", "r")
            content = read_file.read()
            print("Content of the config file are:\n")
            print(content)
            read_file.flush()
            read_file.close()
            return True
        except:
            return False

