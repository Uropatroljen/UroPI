import UroCommand_pb2 as UroCommand

class c_ProtoBuf:
    
    #Takes the message object Command and serilize it to a bytestring
    def SerilizeMessage(self,command:UroCommand.Command): 
        message = command.SerializeToString()
        return message

    #Takes bytes from socket client and deserilize the message object using protobuf
    def DeserilizeMessage(self,message:bytes):
        command = UroCommand.Command()
        command.ParseFromString(message)
        return command
