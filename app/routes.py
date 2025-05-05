from flask import Blueprint, jsonify
import json
import os

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/threats")
def get_threats():
    file_path = os.path.join(os.path.dirname(__file__), "data", "threat_data.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    return jsonify(data)

@api_bp.route("/")
def health():
    return "Backend is alive."
