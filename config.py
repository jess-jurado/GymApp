import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# Configuración centralizada
SECRET_KEY = os.getenv("SECRET_KEY", "mi_clave_secreta_por_defecto")

def get_db_connection():
    try:
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gymapp.db')
        conn = sqlite3.connect(db_path, check_same_thread=False)
        return conn
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        raise