from flask import Blueprint, request, jsonify
from authors_app.models.user import User, db
from authors_app.extensions import bcrypt, jwt
import validators
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, JWTManager
# from email_validator import validate_email, EmailNotValidError

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
jwt = JWTManager()
@auth.route('/register', methods=["POST"])
def register():
    try:
        data = request.json
        required_fields = ["first_name", "last_name", "email", "image", "biography", "user_type", "password", "contact"]
        
        if not all(field in data for field in required_fields):
            return jsonify({'error': "All fields are required"}), 400
        
        if len(data["password"]) < 6:
            return jsonify({'error': "Your password must have at least 6 characters"}), 400
        
        if User.query.filter_by(email=data["email"]).first():
            return jsonify({'error': "The email already exists"}), 400
        
        new_user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            password=bcrypt.generate_password_hash(data["password"]).decode('utf-8'),
            contact=data["contact"],
            biography=data["biography"],
            user_type=data["user_type"],
            image=data["image"]
        )
        
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@auth.route('/users', methods=["GET"])
def get_all_users():
    try:
        users = User.query.all()
        serialized_users = [
            {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'image': user.image,
                'biography': user.biography,
                'user_type': user.user_type,
                'contact': user.contact
            }
            for user in users
        ]
        
        return jsonify({'users': serialized_users}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth.route('/user/<int:user_id>', methods=["GET"])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        serialized_user = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'image': user.image,
            'biography': user.biography,
            'user_type': user.user_type,
            'contact': user.contact
        }
        
        return jsonify({'user': serialized_user}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth.route('/login', methods=["POST"])
def login():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")

# Making the query against the first record
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            access_token  = create_access_token(identity=user.id)
            return jsonify({
                'access_token': access_token,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'username': f'{user.first_name} {user.last_name}'
                }
            }), 200
        else:
            return jsonify({'error': 'Invalid email or password'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth.route('/edit/<int:user_id>', methods=["PUT"])
def edit_user(user_id):
    try:
        data = request.json
        user = User.query.get(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        for field in ["first_name", "last_name", "email", "image", "biography", "user_type", "password", "contact"]:
            if field in data:
                setattr(user, field, data[field])

        if 'password' in data and len(data['password']) < 6:
            return jsonify({'error': 'Password must have at least 6 characters'}), 400
        
        if 'password' in data:
            user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        db.session.commit()

        return jsonify({'message': 'User updated successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@auth.route('/delete/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Secret key for encoding and decoding the token
SECRET_KEY = 'A0703b91L08e9K9JV'

def generate_token(user_id):
    try:
        # Set the expiration time for the token (e.g., 1 day)
        expiration_time = datetime.utcnow() + timedelta(days=1)

        
        # payload is a JSON object that contains assertions about the user or any entity
        # In this case the payload is containing user_id and expiration time
        payload = {
            'user_id': user_id,
            'exp': expiration_time
        }

        # Encode the payload and create the token jwt(JSON Web Tokens)
        # algorithm is the method used for signing and verifying the token
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return token

    except Exception as e:
        # Handle token generation error
        print(f"Token generation failed: {str(e)}")
