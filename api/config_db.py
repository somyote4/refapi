import  pymssql #, urllib, pyodbc
from sqlalchemy import  create_engine
class  MSconfig:
    server = '192.168.17.89' 
    username = 'sa'     
    password = 'T@st1234'
    database = ''
    #conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD='+ password+';DATABASE='+database
    def con_str(self):
        #self.conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+MSconfig.server+';UID='+ MSconfig.username +';PWD='+ MSconfig.password +';DATABASE='+ MSconfig.database
        self.conn_string = 'mssql+pymssql://'+ MSconfig.username +':'+ MSconfig.password +'@'+ MSconfig.server +'/'+ MSconfig.database
        return self.conn_string

class AzureSQLDatabase(object):
    connection =  None
    engine = None
    #cursor = None

    
    def __init__(self):
        constr=MSconfig()
        
        self.engine = create_engine(constr.con_str())
        self.connection = self.engine.connect()
        
        #self.params = urllib.parse.quote_plus(constr.con_str())
        #self.engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % self.params)
        
        #self.connection = pyodbc.connect(constr.con_str())
        #self.cursor = self.connection.cursor()
        
    def query(self, query):
        return self.connection.execute(query) #

    #def Nquery(self, query):
    #    return self.connection.execute(query) #self.cursor.execute(query)

    def commit(self):
        return self.connection.commit()

    def __del__(self):
        self.connection.close()