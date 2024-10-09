from flask_cors import CORS

def configure_cors(app):
    # This allows cross-origin requests from your Vue frontend (http://localhost:8080)
    CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})