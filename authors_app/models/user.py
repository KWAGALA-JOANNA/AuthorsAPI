# importing the db
from authors_app.extensions import db
from datetime import datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
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
    password= db.Column(db.Text, nullable=False)
    contact = db.Column(db.Integer, nullable=False, unique=True)
    biography = db.Column(db.Text, nullable=True)
    user_type = db.Column(db.String(50), default='author') #author , admin
    image = db.Column(db.String(255), nullable=True)
    # company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    # company = db.relationship('Company', backref ='users') 
    # books = db.relationship('Book', backref='user')
    
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    # creating a constructor so that new instances and new users are tracked
    
    def __init__(self, first_name, last_name, email, password, contact, biography, user_type, image):
        super(User, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.contact = contact
        self.biography = biography
        self.user_type = user_type
        self.image = image
        

# creating a custom function that concatenates the user's first name and last name
def get_full_name(self):
    
    return f'{self.first_name} {self.last_name}'
def check_password(self, password):
    return bcrypt.check_password_hash(self.password, password)

        
        
    