import socket
from _thread import *
from CommandHandler import c_CommandHandler

class c_Server:
    commandHandler = c_CommandHandler()
    modelNumber = "SAS9"

    def __init__(self,host:str,port:int):
        self.Start(host,port)
  
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
                self.commandHandler.CommandRunner(data)
            except:
                #Kill thread
                return
    #Sending message to client
    def __SendMessage(self,connection: socket.socket,message: bytes):
        """send message to socket client"""
        connection.send(message)
              connection.send(message)
        connection.close()