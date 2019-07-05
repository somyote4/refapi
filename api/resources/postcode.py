from flask_restful import Api, Resource, reqparse, fields, marshal
#from flask_httpauth import HTTPBasicAuth
from datetime import datetime
#import json
from api.config_db import *

MSconfig.database = 'ref_DB'

postcode_fields = {
    'Changwat_TH': fields.String,
    'Amphoe_TH': fields.String,
    'Tambon_TH': fields.String,
    'PostCode': fields.String,
    'Remark': fields.String
}

class PostChangwatAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('changwat', type=str, required=True, help='The API URL\'s Chanwat Name ?')
        #self.reqparse.add_argument('AA', type=str,  help='The API URL\'s AA Name ?')
        super(PostChangwatAPI).__init__()
    
    def get(self, changwat):
        try:
            params = (changwat) 
            sql =   "SELECT * FROM PostCode WHERE Changwat_TH like '"+ params +"'"  #and AA = ? " 
            conn = AzureSQLDatabase()
            cursor = conn.query(sql) 

            columns =[col for col in cursor.keys()]
            postcodes = []
            for row in cursor.fetchall():
                postcodes.append(dict(zip(columns, row)))
            return { 
                'PostCode': marshal(postcodes, postcode_fields)
            },200
        except Exception as e:
            return {'error': str(e)}

class PostCodeAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('postcode', type=str, required=True, help='The API URL\'s Postcode ?')
        #self.reqparse.add_argument('AA', type=str,  help='The API URL\'s AA Name ?')
        super(PostCodeAPI).__init__()
    
    def get(self, postcode):
        try:
            params = (postcode) 
            sql =   "SELECT * FROM PostCode WHERE PostCode like '"+ params +"'"  #and AA = ? " 
            conn = AzureSQLDatabase()
            cursor = conn.query(sql) 

            columns =[col for col in cursor.keys()]
            pcode = []
            for row in cursor.fetchall():
                pcode.append(dict(zip(columns, row)))
            return { 
                'PostCode': marshal(pcode, postcode_fields)
            },200
        except Exception as e:
            return {'error': str(e)}