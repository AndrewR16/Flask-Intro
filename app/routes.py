from flask import Blueprint, jsonify

bp = Blueprint("routes", __name__)

@bp.get("/")
def index():
    return jsonify({"message": "Task Manager API — up and running"})
