# app extensions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt # for hashing our passwords
# from flask_jwt_extended import JWTManager #for creating tokens
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, JWTManager

db = SQLAlchemy() #handles the ORM related activities
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()
