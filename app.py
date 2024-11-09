from flask import Flask, jsonify, request


app = Flask(__name__)

users = [
    {"id": 1, "name": "Nippu", "age": 12},
    {"id": 2, "name": "Poingu", "age": 123},
    {"id": 3, "name": "Suresh", "age": 456},
    {"id": 4, "name": "Ravi", "age": 789},
    {"id": 5, "name": "Pavan", "age": 1011}
]


# get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# get particular user (params)
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({
        "error": "User not found"
    }), 404


# create a user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "id": users[-1]["id"]+1 if users else 1,
        "name": data["name"],
        "age": data["age"]
    }
    users.append(new_user)
    return jsonify(new_user), 201


# update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user["name"] = data.get("name", user["name"])
        user["age"] = data.get("age", user["age"])
        return jsonify(user)
    return jsonify({
        "error": "User not found"
    }), 404


# delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] == user_id]
    return jsonify({
        "message": "User deleted"
    }), 200

