from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import api_bp  # ✅ make sure it's api_bp
    app.register_blueprint(api_bp, url_prefix="/api")  # ✅ /api prefix applied

    return app
