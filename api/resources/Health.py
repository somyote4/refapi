from flask_restful import Api, Resource, reqparse, fields, marshal

from datetime import datetime

from api.config_db import *
from sqlalchemy import  create_engine

MSconfig.database = 'ref_DB'

Health_fields = {
    'Health_Code': fields.String,
    'Healtlh_Name': fields.String,
    'Health_type': fields.String,
    'Ministry': fields.String,
    'Department': fields.String,
    'Bed': fields.String,
    'Status': fields.String,
    'Address': fields.String,
    'Changwat': fields.String,
    'Amphoe': fields.String,
    'Tumbon': fields.String,
    'Moo': fields.String,
    'Telephone': fields.String,
    'Fax': fields.String,
    'PostCode': fields.String,
    'Remark': fields.String
}

class HealthAPI(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('changwat', type=str, required=True, help='The API URL\'s Chanwat Name ?')
        #self.reqparse.add_argument('AA', type=str,  help='The API URL\'s AA Name ?')
        super(HealthAPI).__init__()
    
    def get(self, changwat):
        try:
            params = (changwat) 
            sql =   "SELECT * FROM View_HealthService WHERE changwat like '%"+params+"%'"  
            conn = AzureSQLDatabase()
        
            #connection = 'mssql+pymssql://sa:T@st1234@192.168.17.89/ref_DB'
            #engine = create_engine(connection)
            #cursor = engine.execute(sql)
                    
            cursor = conn.query(sql) 
            columns =[col for col in cursor.keys()]
            #columns = [desc[0] for desc in cursor.description]       
            

            Healths = []
            for row in cursor.fetchall():
                Healths.append(dict(zip(columns, row)))

            return { 
                'MOPH-HealthService': marshal(Healths, Health_fields)
            },200
        except Exception as e:
            return {'error': str(e)}
