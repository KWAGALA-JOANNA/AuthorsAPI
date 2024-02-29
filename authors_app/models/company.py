from authors_app import db

class Company():
    __tablename__ ='company'
    
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.string(255), nullable=False, unique=True)
    user_id = db.column(db.Interger, db.foreign_key('users.id'))
    user = db.relationship('User', back_populates='Company')
    