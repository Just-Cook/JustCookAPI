import pymysql


#CLEARDB_DATABASE_URL = 'mysql://b3181b88ca232f:9d9b220c@us-cdbr-east-05.cleardb.net/heroku_1047d87c3352696?reconnect=true'
DATABASE_URL = 'mysql+pymysql://root:@localhost/dbjustcook'
# SQLAlchemy monitorará modificações de objetos
SQLALCHEMY_TRACK_MODIFICATIONS = True
