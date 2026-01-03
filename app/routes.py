from app import app
from app.controller import UserController, TodoController
from flask import request

# --- ROUTE USER & LOGIN ---
@app.route('/users', methods=['POST'])
def users():
    return UserController.store()

@app.route('/login', methods=['POST'])
def login():
    return UserController.login()

# --- ROUTE TODO ---
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'GET':
        return TodoController.index()
    else:
        return TodoController.store()

@app.route('/todo/<id>', methods=['PUT', 'DELETE'])
def todo_detail(id):
    if request.method == 'PUT':
        return TodoController.update(id)
    else:
        return TodoController.delete(id)