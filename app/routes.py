from flask import Blueprint, jsonify
import json
import os
from .ml_model import predict_threat
from .optimizer import get_optimal_route

api = Blueprint("api", __name__)

@api.route("/threats")
def get_threats():
    path = os.path.join(os.path.dirname(__file__), "data", "threat_data.json")
    with open(path) as f:
        data = json.load(f)
    return jsonify(data)

@api.route("/route")
def get_route():
    return jsonify(get_optimal_route())

@api.route("/predict")
def predict():
    return jsonify(predict_threat())
