from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory storage
users = []

# Create user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User created successfully"}), 201

# Read users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# Update user
@app.route("/users/<int:index>", methods=["PUT"])
def update_user(index):
    users[index] = request.get_json()
    return jsonify({"message": "User updated successfully"}), 200

# Delete user
@app.route("/users/<int:index>", methods=["DELETE"])
def delete_user(index):
    users.pop(index)
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
