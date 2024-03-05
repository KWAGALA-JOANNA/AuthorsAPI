class Config:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:@localhost/flaskauthors'
    # pymsql is the driver and mysql is the dialect 
    # dialect+driver://username:password@host:port/database this is the format
    # the default username is 'root' if your working with xampp
    # the server will be 'localhost' and db is the name of the database created in xampp
   
    