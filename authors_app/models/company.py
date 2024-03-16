from authors_app.extensions import db
from datetime import datetime

# creating new class for the book model.
class Company(db.Model):
    __tablename__ ='companies'
    
    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(255), nullable=False, unique=True)
    origin = db.Column(db.String(100))
    description = db.Column(db.String(255))
    
    # An author can have more than one company so we create a one to many relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # backref/back_populates helps the user accessthe different companies
    user = db.relationship('User', backref='companies')
    
    # creating timestamps
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    
    # company constructors
    # the ID well automatically be included
    def __init__(self, name, origin, description, user_id):
        super(Company, self).__int__()
        self.name = name
        self.origin = origin
        self.description = description
        self.user_id = user_id
    
#    string representation for the comapanies 
    def __repr__(self):
        return f"{self.name}, {self.origin}"
    