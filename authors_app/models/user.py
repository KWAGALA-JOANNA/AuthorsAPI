# importing the db
from authors_app.extensions import db
from datetime import datetime
# creating class user and inheriting the model
class User(db.Model ):
    __tablename__ ='users' # renaming the user class
    # creating an instance
    # nullable means the field is either required or not
    # primarykey and unique are constraints
    # first and last_
    id= db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(50), nullable=False)
    last_name= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique=True)
    password= db.Column(db.String(100), nullable=False, unique=True)
    contact = db.Column(db.Integer, nullable=False, unique=True)
    biography = db.Column(db.String(1000))
    user_type = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    company = db.relationship('companies', back_populates ='users')
    books = db.relationship('books', back_populates='users')
    
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    