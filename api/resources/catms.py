#from flask import  request, jsonify, abort, make_response, url_for
from flask_restful import Api, Resource, reqparse, fields, marshal
#from flask_httpauth import HTTPBasicAuth
from datetime import datetime

import json
from api.config_db import *
#from sqlalchemy import   Integer, String

MSconfig.database = 'ref_DB'

CATM_fields = {
    'CATM_UKEY': fields.Integer,
    'CC': fields.String,
    'Changwat_TH': fields.String,
    'Changwat_EN': fields.String,
    'AA': fields.String,
    'Amphoe_TH': fields.String,
    'Amphoe_EN': fields.String,
    'TT': fields.String,
    'Tumbon_TH': fields.String,
    'Tumbon_EN': fields.String,
    'MM': fields.String,
    'Moo_TH': fields.String,
    'Moo_EN': fields.String,
    'CATM_TDATE':fields.Integer
}

class CATMListAPI(Resource):
    """
    API Resource for listing all tasks from the database.
    Provides the endpoint for creating new tasks
    :param: none
    :type a json object
    :return task, status_code
    """

    #decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('changwat', type=str, required=True, help='The API URL\'s Chanwat Name ?')
        #self.reqparse.add_argument('AA', type=str,  help='The API URL\'s AA Name ?')
        super(CATMListAPI).__init__()

    def get(self, changwat):
        try:
          
            #MSconfig.database = 'ref_DB'
            #params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.17.89;DATABASE=ref_DB;UID=sa;PWD=T@st1234")
            #engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
            params = (changwat) 
            sql =   "SELECT * FROM View_CATM_Name WHERE Changwat_TH like '"+ params +"'" #and AA = ? " 
                  #u"select task_id, task_name, task_description, task_date, task_due, task_reminder, task_completed, " \
                  #u"task_userid from tasks " \
                  #u"WHERE task_date > ?"
            conn = AzureSQLDatabase()
            cursor = conn.query(sql) #, changwat)
            #connection = engine.connect()
            #cursor = connection.execute(sql)
        
            #columns = [column[0] for column in cursor.column_descriptions]
            columns =[col for col in cursor.keys()]
            CATMs = []
            for row in cursor.fetchall():
                CATMs.append(dict(zip(columns, row)))
            return { 
                'CATM': marshal(CATMs, CATM_fields)
            },200
        except Exception as e:
            return {'error': str(e)}

r_fields = {
    'RCODE_CODE': fields.String,
    'RCODE_DESC': fields.String,
    'RCODE_EDESC': fields.String,
    'Changwat_TH': fields.String,
    'Changwat_EN': fields.String,
    'RCODE_TYPE': fields.Integer,
    'TYPE': fields.String
}


class RCodeAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('changwat', type=str, required=True, help='The API URL\'s Chanwat Name ?')
        super(RCodeAPI).__init__()

    def get(self, changwat):
        try:
           
            params = (changwat) 
            sql =   "SELECT * FROM View_rcode WHERE Changwat_TH like '"+ params +"'" #and AA = ? " 
            conn = AzureSQLDatabase()
            cursor = conn.query(sql) 

            columns =[col for col in cursor.keys()]
            rcodes = []
            for row in cursor.fetchall():
                rcodes.append(dict(zip(columns, row)))
            return { 
                'rcode': marshal(rcodes, r_fields)
            },200
        except Exception as e:
            return {'error': str(e)}
