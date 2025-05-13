from flask import Blueprint, jsonify
import json
import os

api_bp = Blueprint("api", __name__, url_prefix="/api")  # ✅ must be named api_bp
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

@api_bp.route("/threats")  # ✅ fixed name
def get_threats():
    with open(os.path.join(DATA_DIR, 'threat_data.json')) as f:
        data = json.load(f)
    return jsonify(data)

@api_bp.route("/route")  # ✅ used by ThreatMap for coordinates
def get_route():
    coords = [
        {"lat": 12.9, "lng": 80.1},
        {"lat": 13.0, "lng": 80.2},
        {"lat": 13.1, "lng": 80.3},
        {"lat": 13.2, "lng": 80.4}
    ]
    return jsonify(coords)

@api_bp.route("/route-nodes")  # ✅ used by App.tsx for ["A", "B", "C"]
def get_route_nodes():
    return jsonify(["A", "B", "C", "D"])

@api_bp.route("/predict")  # ✅ prediction endpoint
def predict_threat_level():
    prediction = {
        "prediction": "High Threat",
        "confidence": 0.92
    }
    return jsonify(prediction)

@api_bp.route("/")  # ✅ backend health
def health():
    return "Backend is alive."
