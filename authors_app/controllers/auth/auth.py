from flask import Blueprint, request, jsonify
from authors_app.models.user import User, db
from authors_app.extensions import bcrypt

# Create a blueprint
auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

# Define the registration endpoint
@auth.route('/register', methods=["POST"])
def register():
    try:
        # Extract user data from the request JSON
        data = request.json
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        image = data.get("image")
        biography = data.get("biography")
        user_type = data.get("user_type")
        password = data.get("password")
        contact = data.get("contact")  # Assuming you have a contact field

        # Validate input data
        if not all([first_name, last_name, email, image, biography, user_type, password, contact]):
            return jsonify({'error': "All fields are required"}), 400
        if len(password) < 6:
            return jsonify({'error': "Your password must have at least 6 characters"}), 400
        if User.query.filter_by(email=email).first():
            return jsonify({'error': "The email already exists"}), 400

        # Create a new instance of the User model
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=bcrypt.generate_password_hash(password).decode('utf-8'),
            contact=contact,
            biography=biography,
            user_type=user_type,
            image=image
        )

        # Add the new user instance to the database session
        db.session.add(new_user)

        # Commit the session to save the changes to the database
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
    
    # Define the login endpoint
@auth.route('/login', methods=["POST"])
def login():
    try:
        # Extract email and password from the request JSON
        data = request.json
        email = data.get("email")
        password = data.get("password")

        # Retrieve the user by email
        user = User.query.filter_by(email=email).first()

        # Check if the user exists and the password is correct
        if user and bcrypt.check_password_hash(user.password, password):
            # Return a success response
            return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
        else:
            # Return an error response if authentication fails
            return jsonify({'error': 'Invalid email or password'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
    
    
    # Define the edit user endpoint
@auth.route('/edit/<int:user_id>', methods=["PUT"])
def edit_user(user_id):
    try:
        # Extract user data from the request JSON
        data = request.json
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Update user fields if provided in the request
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'email' in data:
            # Check if the new email already exists
            new_email = data['email']
            if new_email != user.email and User.query.filter_by(email=new_email).first():
                return jsonify({'error': 'The email already exists'}), 400
            user.email = new_email
        if 'image' in data:
            user.image = data['image']
        if 'biography' in data:
            user.biography = data['biography']
        if 'user_type' in data:
            user.user_type = data['user_type']
        if 'password' in data:
            password = data['password']
            if len(password) < 6:
                return jsonify({'error': 'Password must have at least 6 characters'}), 400
            user.password = bcrypt.generate_password_hash(password).decode('utf-8')
        if 'contact' in data:
            user.contact = data['contact']

        # Commit the session to save the changes to the database
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'User updated successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
    # delete user endpoint
@auth.route('/delete/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit() #pushes to the database

        return jsonify({'message': 'User deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500



