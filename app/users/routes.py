from flask import jsonify, request
from app.users import bp
from app.users.services import fetch_user, create_user

@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    success, response = fetch_user(user_id)
    if success:
        return jsonify(response), 200
    else:
        return jsonify(response), 400

@bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    success, response = create_user(data)
    if success:
        return jsonify(response), 201
    else:
        return jsonify(response), 400
