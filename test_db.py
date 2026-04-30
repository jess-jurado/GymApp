from config import get_db_connection

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    print("✅ Conexión a PostgreSQL exitosa!")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ Error de conexión: {e}")