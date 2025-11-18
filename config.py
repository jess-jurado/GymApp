import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Configuración de la conexión a SQL Server
# DB_SERVER = "DESKTOP-RS20AM8\\SQLEXPRESS01"
# DB_NAME = "GymApp"

# def get_db_connection():
#     conn = pyodbc.connect(
#         f"DRIVER={{SQL Server}};SERVER={DB_SERVER};DATABASE={DB_NAME};Trusted_Connection=yes;"
#     )
#     return conn

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )
        return conn
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        raise