from config import get_db_connection

def check_subgrupos():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Ver todos los grupos y subgrupos
    cursor.execute("SELECT DISTINCT Grupo_muscular, Subgrupo_muscular FROM Ejercicios ORDER BY Grupo_muscular, Subgrupo_muscular")
    resultados = cursor.fetchall()
    
    print("📊 Grupos y subgrupos en la base de datos:")
    for grupo, subgrupo in resultados:
        print(f"   - {grupo}: {subgrupo}")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    check_subgrupos()