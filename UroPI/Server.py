import socket
from _thread import *

class c_Server:
    host = '0.0.0.0'
    port = 1883

    def __init__(self):
        self.Start(self.host,self.port)

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
        
    def accept_connections(self, ServerSocket):
        while True:
            Client, address = ServerSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.client_handler, (Client, ))
    
    def client_handler(self,connection: socket.socket):
        while True:
            try:
                data = connection.recv(2048)
                print(data)
                if len(data) != 0:
                    socket.socket.sendall(b"Welcome to the Uro socket")
            except:
                #Kill thread
                return