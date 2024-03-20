from flask import Blueprint, request, jsonify
from authors_app.models.company import Company, db
from authors_app.extensions import bcrypt


# Create a blueprint
company_api = Blueprint('company_api', __name__, url_prefix='/api/v1/companies')

# Define the create company endpoint
@company_api.route('/register', methods=["POST"])
def create_company():
    try:
        # Extract company data from the request JSON
        data = request.json
        name = data.get("name")
        origin = data.get("origin")
        description = data.get("description")
        user_id = data.get("user_id")

        # Validate input data
        if not all([name, origin, user_id]):
            return jsonify({'error': "All fields are required "}), 400

        # Creating a new instance of the Company model
        new_company = Company(
            name=name,
            origin=origin,
            description=description,
            user_id=user_id
        )

        # Adding a new company instance to the database session
        db.session.add(new_company)

        # Committing the session to save the changes to the database
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'Company created successfully', 'company_id': new_company.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Define the get company endpoint
@company_api.route('/get/<int:company_id>', methods=["GET"])
def get_company(company_id):
    try:
        company = Company.query.get(company_id)
        if not company:
            return jsonify({'error': 'Company not found'}), 404
        return jsonify({'message': 'Company obtained successfully', 'company_id': company_id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define the update company endpoint
@company_api.route('/edit/<int:company_id>', methods=["PUT"])
def update_company(company_id):
    try:
        # Extract company data from the request JSON
        data = request.json
        company = Company.query.get(company_id)
        if not company:
            return jsonify({'error': 'Company not found'}), 404

        # Update company fields if provided in the request
        for key, value in data.items():
            setattr(company, key, value)

        # Commit the session to save the changes to the database
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'Company updated successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Define the delete company endpoint
@company_api.route('/delete/<int:company_id>', methods=["DELETE"])
def delete_company(company_id):
    try:
        company = Company.query.get(company_id)
        if not company:
            return jsonify({'error': 'Company not found'}), 404

        db.session.delete(company)
        db.session.commit()

        return jsonify({'message': 'Company deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
