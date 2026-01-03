from app.model.user import Users
from app import response, app, db
from flask import request
from flask_jwt_extended import *
from datetime import datetime, timedelta

# --- FUNGSI REGISTER (DAFTAR) ---
def store():
    try:
        # 1. Ambil data dari Body Postman
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        
        # 2. Masukkan ke wadah (Model Users)
        users = Users(name=name, email=email)
        users.setPassword(password) # Hash password agar aman
        
        # 3. Simpan ke Database
        db.session.add(users)
        db.session.commit()
        
        return response.success('', 'Sukses Menambahkan Data User!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal: ' + str(e))

# --- FUNGSI LOGIN (MASUK) ---
def login():
    try:
        email = request.json['email']
        password = request.json['password']
        
        # 1. Cari user berdasarkan email
        user = Users.query.filter_by(email=email).first()
        
        # 2. Cek apakah user ada DAN passwordnya benar
        if not user or not user.checkPassword(password):
            return response.badRequest([], 'Email atau Password Salah')
        
        
        
        # 3. Buat Token (Tiket Masuk)
        data = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        
        # Token akses & Refresh
        expires = timedelta(days=7)
        
        
        access_token = create_access_token(identity=str(user.id), fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(identity=str(user.id), expires_delta=expires)
        
        return response.success({
            "data": data,
            "token_access": access_token,
            "token_refresh": refresh_token
        }, "Sukses Login!")
        
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal Login: ' + str(e))