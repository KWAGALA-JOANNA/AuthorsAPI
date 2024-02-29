from authors_app import db
class Books():
    __tablename__ = 'books'
    id = db.column(db.Integer, primary_key=True)
    title = db.column(db.string(100), nullable=False)
    description = db.column(db.text)
    price = db.column(db.float)
    number_of_pages = db.column(db.Integer)
    user_id = db.column(db.Integer, db.foreign_key('users.id'))
    user=db.relationship('User', back_populates='Books')
    
    