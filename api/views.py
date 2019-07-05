from flask import Blueprint, request
from flask_restful import Api
from api.resources.Hello import Hello
from api.resources.Category import CategoryResource
from api.resources.postcode import PostChangwatAPI, PostCodeAPI
#from resources.Comment import CommentResource
from api.resources.catms import CATMListAPI , RCodeAPI
from api.resources.Countries import CountriesAPI, CountryAPI
from api.resources.Health import HealthAPI 
import psycopg2, pymssql
#from DBconfig import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash

api_app = Blueprint('api_app', __name__)
#author_app = Blueprint('author_app', __name__)
api = Api(api_app)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/category')
#api.add_resource(CommentResource, '/Comment')

# register the API CATM resources and define endpoints
api.add_resource(CATMListAPI, '/catms/changwat=<string:changwat>', methods=['GET'])#, endpoint='catm')
api.add_resource(RCodeAPI, '/rcodes/changwat=<string:changwat>', methods=['GET'])

# register the API Postcode resources and define endpoints
api.add_resource(PostChangwatAPI, '/postcode/changwat=<string:changwat>', methods=['GET'])
api.add_resource(PostCodeAPI, '/postcode/code=<string:postcode>', methods=['GET'])

# register the API Countries resources and define endpoints
api.add_resource(CountriesAPI, '/countries/continent=<string:continent>', methods=['GET'])
api.add_resource(CountryAPI, '/countries/country=<string:country>',  methods=['GET'])

# register the API Health resources and define endpoints
api.add_resource(HealthAPI, '/health/changwat=<string:changwat>', methods=['GET'])


@api_app.route('/tests')
def users():
	try:
		conn = pymssql.connect(host='192.168.17.89',user='sa',password='T@st1234',database='ref_db')
		# psycopg2.connect(database='test', user='test_user', password='T@st1234', host='localhost', port='5432')
		cursor = conn.cursor()
		params = 'นนทบุรี';
		sql =   "SELECT * FROM View_HealthService WHERE changwat like '%"+params+"%';"  
		cursor.execute(sql) #("SELECT * FROM author")
		rows = cursor.fetchall()
		columns = [desc[0] for desc in cursor.description]

		H = []
		for result in rows:
			H.append(dict(zip(columns,result)))
	

		resp = jsonify(H)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



