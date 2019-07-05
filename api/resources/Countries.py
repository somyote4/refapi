from flask_restful import Api, Resource, reqparse, fields, marshal
#from flask_httpauth import HTTPBasicAuth
from datetime import datetime
#import json
from api.config_db import *

MSconfig.database = 'ref_DB'

countries_fields = {
    'Num-3': fields.String,
    'Alpha-2': fields.String,
    'Region-Num': fields.String,
    'Continental_TH': fields.String,
    'Continental_EN': fields.String,
    'Sub-Region-Num': fields.String,
    'Sub-Continental_TH': fields.String,
    'Sub-Continental_EN': fields.String,
    'Countries_TH' : fields.String,
    'Countries_EN' : fields.String,
}

class CountryAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('country', type=str, required=True, help='The API URL\'s country Name ?')
        #self.reqparse.add_argument('AA', type=str,  help='The API URL\'s AA Name ?')
        super(CountryAPI).__init__()
    
    def get(self, country):
        try:
            params = (country) 
            sql =   "SELECT * FROM View_Countries WHERE Countries_EN = '"+ params +"'"  #and AA = ? " 
            conn = AzureSQLDatabase()
            cursor = conn.query(sql) 

            columns =[col for col in cursor.keys()]
            country_code = []
            for row in cursor.fetchall():
                 country_code.append(dict(zip(columns, row)))
            return { 
                'NSO:Countries': marshal(country_code,countries_fields)
            },200
        except Exception as e:
            return {'error': str(e)}

class CountriesAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('continent', type=str, required=True, help='The API URL\'s continent Name ?')
        #self.reqparse.add_argument('AA', type=str,  help='The API URL\'s AA Name ?')
        super(CountriesAPI).__init__()
    
    def get(self, continent):
        try:
            params = (continent) 
            sql =   "SELECT * FROM View_Countries WHERE Continental_EN like '"+ params +"'"  #and AA = ? " 
            conn = AzureSQLDatabase()
            cursor = conn.query(sql) 

            columns =[col for col in cursor.keys()]
            countries_code = []
            for row in cursor.fetchall():
                 countries_code.append(dict(zip(columns, row)))
            return { 
                "NSO":"Countries",'Countries': marshal(countries_code,countries_fields)
            },200
        except Exception as e:
            return {'error': str(e)}
