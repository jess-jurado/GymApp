from config import get_db_connection

def verificar_ejercicios():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    print("📊 EJERCICIOS EN LA BASE DE DATOS:")
    print("=" * 50)
    
    # Contar total de ejercicios
    cursor.execute("SELECT COUNT(*) FROM Ejercicios")
    total = cursor.fetchone()[0]
    print(f"Total de ejercicios: {total}")
    print()
    
    # Obtener todos los ejercicios agrupados por grupo muscular
    cursor.execute("""
        SELECT Grupo_muscular, Subgrupo_muscular, Nombre_ejercicio, imagen_url 
        FROM Ejercicios 
        ORDER BY Grupo_muscular, Subgrupo_muscular, Nombre_ejercicio
    """)
    
    ejercicios = cursor.fetchall()
    
    grupo_actual = ""
    for ejercicio in ejercicios:
        grupo, subgrupo, nombre, imagen = ejercicio
        
        if grupo != grupo_actual:
            print(f"🎯 GRUPO: {grupo}")
            grupo_actual = grupo
        
        print(f"   ├── Subgrupo: {subgrupo}")
        print(f"   │   └── Ejercicio: {nombre}")
        print(f"   │       └── Imagen: {imagen}")
        print()
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    verificar_ejercicios()