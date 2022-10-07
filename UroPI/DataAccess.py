import sqlite3
from pandas import array
from setuptools import Command
import UroCommand_pb2 as uroCommand

class c_DataAccess:
    
    con : sqlite3.Connection
    cur : sqlite3.Cursor
    def __init__(self) -> None: 
        try:
            self.con = sqlite3.connect("hoturo.db")
            self.cur = self.con.cursor()
        except:
            pass
        
    def InsertClient(self, client : uroCommand.Client) -> None:
        """Insert client into database"""
        try:
            #With interpolation we create an insert command
            if client.imei and client.token is None :
                return
            #create and execute command
            self.cur.execute(f"""
                            INSERT INTO clients VALUES
                            ('{client.imei}','{client.token}')
                            """)
            #commit the execute command
            self.con.commit()
        except error as error:
                print(error)
    
    
    def GetClients(self): 
        """Return list of clients"""
        #creating command
        allClients = []
        res = self.cur.execute("""
                         SELECT * FROM clients
                         """)
        rows = res.fetchall()
        if len(rows) <= 0 :
            return None
        clients = uroCommand.Client[rows.count]
        for row in rows : 
            allClients.append(uroCommand.Client(row["token"],row["imei"]))
        return allClients 
            
        
        
        
        
    
    