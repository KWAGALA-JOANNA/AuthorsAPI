from flask import Blueprint, request, jsoonify
from app.models import users 
# creating an object for class
auth = Blueprint(auth, __name__, url_prefix('api/vl/auth'))
@auth.route('register', methods=['POST'])
def register_user():
    first_name=request.json['first_name']
    last_name=request.json['last_name']
    email=request.json['email']
    contact=request.json['contact']
    password=request.json['password']
    image=request.json['image']
    biography=request.json['biography']
    user_type=request.json['user_type']
    
    created_at=request.json['created_at']
    updated_at=request.json['updated_at']
    
    # checking for validations
    # doing validation for one by one
    if  not first_name:
        return jsonify(('error:' 'your first_name is required'))
    
    if  not last_name:
        return jsonify(('error:' 'your last_name is required'))
    
    if  not email:
        return jsonify(('error:' 'your email is required'))
    
    if  not contact:
        return jsonify(('error:' 'your contact is required'))
    
    if  len password < 8:
        return jsonify(('error:' 'your password must have atleast 8 characters'))
    
    if  not biography:
        return jsonify(('error:' 'your first_name is required'))
    
    if  not image:
        return jsonify(('error:' 'your image is required'))
    
    if  not user_type:
        return jsonify(('error:' 'your user_type is required'))
    
    if  user_type == 'author' and not biography:
        return jsonify(('error:' 'your biography is required')) #this is supposed tobe for the author
    
    if user.query.filter_by(email=email).first():
        return jsoonify(('error:' 'This email already exists')) #this is a constraint for emails         
    
    #inserting into the table
    user = User(first_name=first_name)           
    
    