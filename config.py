import os

class Config(object):
    # KITA TULIS MANUAL LANGSUNG (HARDCODE)
    # Supaya tidak ada lagi error 'None'
    
    HOST = "localhost"
    DATABASE = "db_mytodo_api"
    USERNAME = "root"
    PASSWORD = ""  # Biarkan kosong jika pakai XAMPP standar
    
    # Membuat URL koneksi manual
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    # JWT Key manual
    JWT_SECRET_KEY = "rahasia_negara_konoha"