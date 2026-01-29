from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# 1. Health check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask API is running"}), 200


# 2. Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# 3. Get single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# 4. Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    new_user = {
        "id": users[-1]["id"] + 1,
        "name": data["name"]
    }

    users.append(new_user)
    return jsonify(new_user), 201


# 5. Delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"}), 200

    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
