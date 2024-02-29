# importing the db
from authors_app import db

# creating class user and inheriting the model
class User(db.Model ):
    __tablename__ ='users' # renaming the user class
    # creating an instance
    # nullable means the field is either required or not
    # primarykey and unique are constraints
    # first and last_
    Id= db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(50), nullable=False)
    last_name= db.column(db.String(100), nullable=False)
    email= db.column(db.string(100), nullable=False, unique=True)
    password= db.column(db.string(100), nullable=False, unique=True)
    contact = db.column(db.Integer(10), nullable=False, unique=True)
    user_type = db.column(db.string(50), nullable=False)
    image = db.column(db.String(255), nullable=True)
    company = db.relationship('Company', back_populates ='User')
    books = db.relationship('Books', back_populates='User')
    books = db.relationship('Books', back_populates='User')