from flask import Blueprint, jsonify
import json
import os
import networkx as nx

api_bp = Blueprint("api", __name__)

@api_bp.route("/threats")
def get_threats():
    file_path = os.path.join(os.path.dirname(__file__), "data", "threat_data.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    return jsonify(data)

@api_bp.route("/route")
def get_route():
    graph_path = os.path.join(os.path.dirname(__file__), "data", "graph.json")
    with open(graph_path, "r") as f:
        graph_data = json.load(f)

    G = nx.Graph()
    for edge in graph_data["edges"]:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    try:
        path = nx.dijkstra_path(G, graph_data["start"], graph_data["end"])
        return jsonify({"path": path})
    except nx.NetworkXNoPath:
        return jsonify({"error": "No path found"}), 404

@api_bp.route("/")
def health():
    return "Backend is alive."
