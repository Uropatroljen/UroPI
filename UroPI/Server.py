import socket
from _thread import *
from ConfigManager import c_ConfigManager
from ProtoBufHelper import c_ProtoBuf
import hashlib
from CommandHandler import c_CommandHandler

class c_Server:
    commandHandler = c_CommandHandler()
    modelNumber = "SAS9"
    __configManager : c_ConfigManager 
    __host = ''
    __port = 1883

    def __init__(self,host:str,port:int):
        self.Start(host,port)
  
    #def __init__(self, configManager : c_ConfigManager):
        #TODO Errorhandling
    #    self.__configManager = configManager
    #    self.__host = self.__configManager.GetIp()
    #    self.__port = int(self.__configManager.GetPort())
    #    self.Start(self.__host,self.__port)

    #Start method for the socket server
    #Listen for IOT Client to connect to the server
    #If client connects, create new thread for the client
    def Start(self,host,port):
        
        ServerSocket = socket.socket()
        try:
            ServerSocket.bind((host, port))
        except socket.error as e:
            print(str(e))
        print(f'Server is listing on the port {port}...')
        ServerSocket.listen()
    
        start_new_thread(self.accept_connections, (ServerSocket, ))

        while True:
            inp = input('')
            if inp == "end":
                return
        
    #Accepts the connections if anyone connects
    def accept_connections(self, ServerSocket):
        while True:
            Client, address = ServerSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.client_handler, (Client, ))
    
    #Listens for input from IOT client
    def client_handler(self,connection: socket.socket):
        while True:
            try:
                data = connection.recv(2048)
                #temp = data.decode('utf-8')
                #if(temp == hashlib.sha256(self.modelNumber.encode('utf-8')).hexdigest()):
                    #TODO Send acknowlagement to app
                    #print("Match")
                self.commandHandler.CommandRunner(data)
            except:
                #Kill thread
                return

    #We need to close the connection after we send data so the client.
    #Knows that it is done listing for data
    #TODO Figure out how to send data without closing connection
    def SendMessage(self,connection: socket.socket,message: bytes):
        connection.send(message)
        connection.close()