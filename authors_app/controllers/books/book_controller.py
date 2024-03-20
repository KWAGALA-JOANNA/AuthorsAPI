from flask import Blueprint, request, jsonify
from authors_app.models.book import Book, db
from authors_app.extensions import bcrypt

# Create a blueprint
book_api = Blueprint('book_api', __name__, url_prefix='/api/v1/books')

# Define the create book endpoint
@book_api.route('/register', methods=["POST"])
def create_book():
    try:
        # Extract book data from the request JSON
        data = request.json
        title = data.get("title")
        description = data.get("description")
        price = data.get("price")
        price_unit = data.get("price_unit")
        publication_date = data.get("publication_date")
        isbn = data.get("isbn")
        number_of_pages = data.get("number_of_pages")
        genre = data.get("genre")
        image = data.get("image")
        user_id = data.get("user_id")
        company_id = data.get("company_id")

        # Validate input data
        if not all([title, description, price, price_unit, publication_date, genre]):
            return jsonify({'error': "All required fields are not provided"}), 400

        # Create a new instance of the Book model
        new_book = Book(
            title=title,
            description=description,
            price=price,
            price_unit=price_unit,
            publication_date=publication_date,
            isbn=isbn,
            number_of_pages=number_of_pages,
            genre=genre,
            image=image,
            user_id=user_id,
            company_id=company_id
        )

        # Add the new book instance to the database session
        db.session.add(new_book)

        # Commit the session to save the changes to the database
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'Book created successfully', 'book_id': new_book.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Define the get book endpoint
@book_api.route('/get/<int:book_id>', methods=["GET"])
def get_book(book_id):
    try:
        book = Book.query.get(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404

        return jsonify({'message': 'Book obtained successfully', 'book_id': book_id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define the update book endpoint
@book_api.route('/edit/<int:book_id>', methods=["PUT"])
def update_book(book_id):
    try:
        # Extract book data from the request JSON
        data = request.json
        book = Book.query.get(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404

        # Update book fields if provided in the request
        for key, value in data.items():
            setattr(book, key, value)

        # Commit the session to save the changes to the database
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'Book updated successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Define the delete book endpoint
@book_api.route('/delete/<int:book_id>', methods=["DELETE"])
def delete_book(book_id):
    try:
        book = Book.query.get(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404

        db.session.delete(book)
        db.session.commit()

        return jsonify({'message': 'Book deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
