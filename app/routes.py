from app import app
from app.controller import UserController
from flask import request

@app.route('/users', methods=['POST'])
def users():
    return UserController.store()

@app.route('/login', methods=['POST'])
def login():
    return UserController.login()