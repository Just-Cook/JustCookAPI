import pymysql


#CLEARDB_DATABASE_URL = 'mysql://b640e097c489c1:cf988b90@us-cdbr-east-05.cleardb.net/heroku_9332df0a49f4d18?reconnect=true'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/dbjustcook'
SQLALCHEMY_DATABASE_URI =  'mysql://b640e097c489c1:cf988b90@us-cdbr-east-05.cleardb.net/heroku_9332df0a49f4d18?reconnect=true'
# SQLAlchemy monitorará modificações de objetos
SQLALCHEMY_TRACK_MODIFICATIONS = True
