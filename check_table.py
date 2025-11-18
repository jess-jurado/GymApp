from config import get_db_connection

def check_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)
    
    tables = cursor.fetchall()
    print("📊 Tablas en la base de datos:")
    for table in tables:
        print(f"   - {table[0]}")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    check_tables()