import os

SECRET_KEY='you-will-never-guess' #os.environ['SECRET_KEY']
DB_USERNAME='sa' #os.environ['DB_USERNAME']
DB_PASSWORD='T@st1234'  #os.environ['DB_PASSWORD'] 
DB_HOST='192.168.17.89'#os.environ['DB_HOST'] #T@st1234
DATABASE_NAME='ref_web'  
#DB_URI = "postgresql://%s:%s@%s:5432/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
DB_URI = "mssql+pymssql://sa:T@st1234@192.168.17.89/ref_web"
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
#MYSQL_ROOT_PASSWORD=os.environ['MYSQL_ROOT_PASSWORD']
BLOG_NAME='Reference Data' #os.environ['BLOG_NAME']
BLOG_POST_IMAGES_PATH='../static/images/uploads'#'D:/Python/Code/flogger-master/static/images/uploads' #os.environ['BLOG_POST_IMAGES_PATH']
#DB_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
