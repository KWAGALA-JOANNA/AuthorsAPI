from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authors_app.extensions import db, migrate, bcrypt
from authors_app.controllers.auth.auth import auth
from authors_app.controllers.books.book_controller import book_api
from authors_app.controllers.companies.company_controller import company_api

# Setting up an application factory function and everything must be within the function
def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    # enables us import our Config class
    # enables us to work with the application without showing our configuration
    # defining the class
    
    # Initialising the third-party libraries. we pass in the app and db
    db.init_app (app) 
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    # jwt.init_app(app)
    
    # working with migrations
    
    # importing and registering models
    from authors_app.models.user import User
    from authors_app.models.company import Company
    from authors_app.models.book import Book
    
   
    # testing whether the application works
    @app.route('/')
    def home():
        return "Authors API setup"
 # # registering blueprints
     # registering the blueprint auth
   
    app.register_blueprint(auth)
    app.register_blueprint(book_api)
    app.register_blueprint(company_api)
    return app

    

