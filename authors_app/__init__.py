from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Setting up an application factory function and everything must be within the function
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    db.init_app (app) 
    # migrate.init_app(app, db)
    # bcrypt.init_app(app)
    # jwt.init_app(app)
    
    # # importing and registerinf models
    # from authors_app.models.user import User
    # from authors_app.models.company import Company
    # from authors_app.models.book import Books
    
    # registering blueprints
    # authors_app.register_blueprint(auth)
    # authors_app.register_blueprint(users)
    # authors_app.register_blueprint(company)
      

    # tsting whether the application works
    @app.route('/')
    def home():
        return "Hello World"
    
    return app

    

