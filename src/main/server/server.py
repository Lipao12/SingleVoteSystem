from flask import Flask
from flask_cors import CORS
from src.main.routes.rout import vote_routes_bp 

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

app.register_blueprint(vote_routes_bp)