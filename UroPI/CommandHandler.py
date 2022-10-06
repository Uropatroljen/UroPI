from ProtoBufHelper import c_ProtoBuf
import UroCommand_pb2 as UroCommand
from ConfigManager import c_ConfigManager
from Music import c_Music
from Light import c_Light
import _thread

class c_CommandHandler:
    protoBuf = c_ProtoBuf()
    configman = c_ConfigManager()
    light = c_Light()
    music = c_Music()

    def CommandRunner(self,message:bytes):
        command : UroCommand.Command = self.protoBuf.DeserilizeMessage(message)
        print(command)
        if(command.client.HasField("imei")):
            print("In client")
        elif(command.music.HasField("title")):
            if(command.command == "Play"):
                _thread.start_new_thread(self.music.PlaySong())
            elif(command.command == "Stop"):
                self.music.running = False
        elif(command.light.HasField("state")):
            if(command.light.state == True):
                print("Inside if true")
                self.light.TurnOnLight(command)
            elif(command.light.state == False):
                print("Inside if false")
                self.light.TurnOnLight()
        elif(command.uro.HasField("model")):
            print("In uro")
        elif(command.network.HasField("ssid")):
            #self.configman.SetupNetwork(command.network.ssid,command.network.psw)
            #self.configman.SetNetworkConnection(1,True)
            pass