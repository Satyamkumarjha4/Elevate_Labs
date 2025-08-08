"""
Task 4 : Build a REST API with Flask
Objective: Create a REST API that manages user data.
Tools :Python, Flask, Postman or Curl
Deliverables: Flask app with GET/POST/PUT/DELETE routes

Hints/Mini Guide:
1.Use Flask to create endpoints
2.Store users in a dictionary or in-memory list

Outcome: : API development fundamentals.

Key Concepts: REST, HTTP Methods, Flask
"""

from flask import Flask, jsonify, request, abort
from colorama import init, Fore, Style
import os

init(autoreset=True)
app = Flask(__name__)

users_path = 'Rest-API/users.txt'
users = {}

# -------------------------- File Handling -------------------------- #
def load_users():
    """Load users from file into the dictionary."""
    data = {}
    if not os.path.exists(users_path):
        os.makedirs(os.path.dirname(users_path), exist_ok=True)
        return data
    with open(users_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                user_id, name, email = line.strip().split('||')
                data[int(user_id)] = {'id': int(user_id), 'name': name, 'email': email}
    return data

def save_users():
    """Save current user dictionary to file."""
    with open(users_path, 'w', encoding='utf-8') as file:
        for user in users.values():
            file.write(f"{user['id']}||{user['name']}||{user['email']}\n")

def get_next_id():
    """Generate next unique user ID."""
    return max(users.keys(), default=0) + 1

users = load_users()

# -------------------------- Routes -------------------------- #
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid input: 'name' is required")
    
    name = request.json['name'].strip()
    email = request.json.get('email', '').strip()

    if not name:
        abort(400, description="Name cannot be empty")
    
    user_id = get_next_id()
    user = {'id': user_id, 'name': name, 'email': email}
    users[user_id] = user
    save_users()

    print(Fore.GREEN + f"User created: {user}")
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if not request.json:
        abort(400, description="Invalid input")
    
    user = users.get(user_id)
    if not user:
        abort(404, description="User not found")
    
    name = request.json.get('name', user['name']).strip()
    email = request.json.get('email', user['email']).strip()

    user['name'] = name
    user['email'] = email
    users[user_id] = user
    save_users()

    print(Fore.BLUE + f"User updated: {user}")
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if not user:
        abort(404, description="User not found")

    save_users()
    print(Fore.RED + f"User deleted: {user}")
    return jsonify({'result': True}), 200

# -------------------------- Run App -------------------------- #
if __name__ == '__main__':
    print(Fore.CYAN + "Flask app is running. Access it at http://127.0.0.1:5000/users")
    app.run(debug=True)
