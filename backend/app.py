from flask import Flask, request, jsonify
from models import db, User, Note
from config import Config
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize the database
db.init_app(app)
jwt = JWTManager(app)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Routes for User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Routes for User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'token': access_token}), 200
    return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/notes', methods=['POST'])
@jwt_required()
def create_note():
    current_user_id = get_jwt_identity()  # Get the logged-in user's ID
    data = request.get_json()
    title = data.get('title', '').strip()
    content = data.get('content', '').strip()

    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400

    new_note = Note(title=title, content=content, user_id=current_user_id)
    db.session.add(new_note)
    db.session.commit()
    return jsonify({'message': 'Note created successfully'}), 201


@app.route('/notes', methods=['GET'])
@jwt_required()
def get_notes():
    current_user_id = get_jwt_identity()  # Get the logged-in user's ID
    notes = Note.query.filter_by(user_id=current_user_id).all()
    result = [{'id': note.id, 'title': note.title, 'content': note.content} for note in notes]
    return jsonify(result), 200

@app.route('/notes/<int:note_id>', methods=['GET'])
@jwt_required()
def get_note(note_id):
    current_user_id = get_jwt_identity()  # Get the logged-in user's ID
    note = Note.query.filter_by(id=note_id, user_id=current_user_id).first()
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    return jsonify({'id': note.id, 'title': note.title, 'content': note.content}), 200

@app.route('/notes/<int:note_id>', methods=['PUT'])
@jwt_required()
def update_note(note_id):
    current_user_id = get_jwt_identity()  # Get the logged-in user's ID
    data = request.get_json()
    note = Note.query.filter_by(id=note_id, user_id=current_user_id).first()
    
    if not note:
        return jsonify({'error': 'Note not found'}), 404

    note.title = data.get('title', note.title).strip()
    note.content = data.get('content', note.content).strip()
    db.session.commit()
    return jsonify({'message': 'Note updated successfully'}), 200

@app.route('/notes/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
    current_user_id = get_jwt_identity()  # Get the logged-in user's ID
    note = Note.query.filter_by(id=note_id, user_id=current_user_id).first()
    
    if not note:
        return jsonify({'error': 'Note not found'}), 404

    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Note deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)