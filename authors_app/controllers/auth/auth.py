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

