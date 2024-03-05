from authors_app.extensions import db
from datetime import datetime
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    number_of_pages = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user=db.relationship('users', back_populates='books')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
     
     
    def __init__(self, title, description, pages, user_id):
        self.title = title
        self.description = description
        
        self.user_id = user_id
        self.number_of_pages = number_of_pages
        
    def __repr__(self):
        return f'<Book {self.title}>'