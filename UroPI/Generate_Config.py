import configparser

# CREATE OBJECT
config_file = configparser.ConfigParser()

# ADD SECTION
config_file.add_section("UroSettings")
config_file.add_section("NetworkOptions")
# ADD SETTINGS TO SECTION
config_file.set("UroSettings", "ConnectionString", "0.0.0.0")
config_file.set("UroSettings", "Port", "1883")
config_file.set("NetworkOptions", "ssid", "ukendt")
config_file.set("NetworkOptions", "psk", "Kode1234!")


with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()
    
print("Config file 'configurations.ini' created")


# PRINT FILE CONTENT
read_file = open("configurations.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()