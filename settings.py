import os

SECRET_KEY='you-will-never-guess' #os.environ['SECRET_KEY']
DB_USERNAME=os.environ['DB_USERNAME']
DB_PASSWORD=os.environ['DB_PASSWORD']
DB_HOST=os.environ['DB_HOST']
DATABASE_NAME='ref_web'  
#DB_URI = "postgresql://%s:%s@%s:5432/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
DB_URI = "mssql+pymssql://sa:T@st1234@192.168.17.89/ref_web"
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
#MYSQL_ROOT_PASSWORD=os.environ['MYSQL_ROOT_PASSWORD']
BLOG_NAME=os.environ['BLOG_NAME']
BLOG_POST_IMAGES_PATH=os.environ['BLOG_POST_IMAGES_PATH']
#DB_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
