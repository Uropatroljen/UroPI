from queue import Empty
from ProtoBufHelper import c_ProtoBuf
import UroCommand_pb2 as UroCommand

class c_CommandHandler:
    protoBuf = c_ProtoBuf()

    def CommandRunner(self,message:bytes):
        command : UroCommand.Command = self.protoBuf.DeserilizeMessage(message)
        print(command)
        if(command.client.HasField("imei")):
            print("In client")
        elif(command.music.HasField("title")):
            print("In music")
        elif(command.light.HasField("state")):
            print("In Light")
        elif(command.uro.HasField("model")):
            print("In uro")
        elif(command.network.HasField("ssid")):
            print("In network")
    pass