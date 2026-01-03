from app.model.todo import Todos
from app import response, app, db
from flask import request
from flask_jwt_extended import *

@jwt_required()
def index():
    try:
        user_id = get_jwt_identity() # <-- Perbaikan: Langsung ambil ID
        todos = Todos.query.filter_by(user_id=user_id).all()
        data = formatarray(todos)
        return response.success(data, "Berhasil mengambil data Todo")
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal: ' + str(e))

@jwt_required()
def store():
    try:
        todo_text = request.json['todo']
        desc = request.json['description']
        user_id = get_jwt_identity() # <-- Perbaikan: Langsung ambil ID
        
        new_todo = Todos(user_id=user_id, todo=todo_text, description=desc)
        db.session.add(new_todo)
        db.session.commit()
        
        return response.success('', 'Sukses Menambahkan Todo!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal: ' + str(e))

@jwt_required()
def update(id):
    try:
        todo_text = request.json['todo']
        desc = request.json['description']
        user_id = get_jwt_identity() # <-- Perbaikan: Langsung ambil ID

        todo = Todos.query.filter_by(id=id, user_id=user_id).first()
        if not todo:
            return response.badRequest([], 'Todo tidak ditemukan atau bukan milik Anda')

        todo.todo = todo_text
        todo.description = desc
        db.session.commit()
        
        return response.success('', 'Sukses Update Todo!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal Update: ' + str(e))

@jwt_required()
def delete(id):
    try:
        user_id = get_jwt_identity() # <-- Perbaikan: Langsung ambil ID
        todo = Todos.query.filter_by(id=id, user_id=user_id).first()
        if not todo:
            return response.badRequest([], 'Todo tidak ditemukan')

        db.session.delete(todo)
        db.session.commit()
        
        return response.success('', 'Sukses Hapus Todo!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal Hapus: ' + str(e))

def formatarray(datas):
    array = []
    for i in datas:
        array.append(singleTransform(i))
    return array

def singleTransform(data):
    return {
        'id': data.id,
        'todo': data.todo,
        'description': data.description,
        'created_at': data.created_at,
        'user_id': data.user_id
    }