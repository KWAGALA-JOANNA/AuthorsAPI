from authors_app.extensions import db
from datetime import datetime
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    price_unit = db.Column(db.String(10), nullable=False, default='UGX')
    # date of book publication
    publication_date =db.Column(db.Date, nullable=False)
    # international standard book number
    isbn =db.Column(db.String(30), nullable=True, unique=True)
    number_of_pages = db.Column(db.Integer)
    genre =  db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    user=db.relationship('User', backref='books')
    company=db.relationship('Company', backref='books')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
     
     
    def __init__(self, title, description, price, price_unit, company_id,user_id, image, genre, publication_date, number_of_pages, isbn):
        # evoking the __init__ method/constructor from the super class Book
        # this ensures that any intialisation of the db.model class is 
        # super(Book, self).__init__()
        self.title = title
        self.description = description
        self.price = price
        self.company_id = company_id
        self.genre = genre
        self.price_unit = price_unit
        self.publication_date = publication_date
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.user_id = user_id
        self.image = image
        
    def __repr__(self):
        return f'<Book {self.title}>'