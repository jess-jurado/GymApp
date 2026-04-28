import os
from config import get_db_connection

def init_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        print("🔄 Creando tablas en PostgreSQL...")
        
        # Tabla Usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Usuarios (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre VARCHAR(100) NOT NULL,
                Email VARCHAR(255) UNIQUE NOT NULL,
                Password_hash VARCHAR(255) NOT NULL,
                Confirmado BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabla Ejercicios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ejercicios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre_ejercicio VARCHAR(100) UNIQUE NOT NULL,
                Grupo_muscular VARCHAR(50),
                Subgrupo_muscular VARCHAR(50),
                imagen_url VARCHAR(255)
            )
        ''')
        
        # Tabla Rutinas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Rutinas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Usuario_id INTEGER REFERENCES Usuarios(Id),
                Nombre_rutina VARCHAR(100),
                Dia VARCHAR(20),
                Id_ejercicio INTEGER REFERENCES Ejercicios(id),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabla Historial
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Historial (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Id_ejercicio INTEGER REFERENCES Ejercicios(id),
                Series INTEGER,
                Repeticiones INTEGER,
                Peso DECIMAL(10,2),
                Fecha TIMESTAMP,
                Usuario_id INTEGER REFERENCES Usuarios(Id),
                Calorias INTEGER,
                Duracion_min INTEGER
            )
        ''')
        
        # Tabla Series
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Entrenamiento_id INTEGER,
                Peso DECIMAL(10,2),
                Repeticiones INTEGER,
                Fecha DATE,
                Id_ejercicio INTEGER REFERENCES Ejercicios(id)
            )
        ''')
        
        print("🔄 Extrayendo ejercicios reales desde Assets_gymApp/Imagenes...")
        # Borrar ejercicios anteriores para evitar duplicados si se ejecuta de nuevo
        cursor.execute("DELETE FROM Ejercicios")
        
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Assets_gymApp', 'Imagenes')
        if os.path.exists(base_dir):
            for grupo in os.listdir(base_dir):
                grupo_path = os.path.join(base_dir, grupo)
                if os.path.isdir(grupo_path):
                    for subgrupo in os.listdir(grupo_path):
                        subgrupo_path = os.path.join(grupo_path, subgrupo)
                        if os.path.isdir(subgrupo_path):
                            for file in os.listdir(subgrupo_path):
                                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                                    nombre_base = os.path.splitext(file)[0]
                                    nombre_ejercicio = nombre_base.replace('_', ' ')
                                    try:
                                        cursor.execute('''
                                            INSERT INTO Ejercicios (Nombre_ejercicio, Grupo_muscular, Subgrupo_muscular, imagen_url)
                                            VALUES (?, ?, ?, ?)
                                        ''', (nombre_ejercicio, grupo, subgrupo, nombre_base))
                                    except Exception as e:
                                        print(f"   ⚠️ Error insertando '{nombre_ejercicio}': {e}")
        
        conn.commit()
        print("✅ ¡Base de datos inicializada correctamente!")
        print("✅ Tablas creadas")
        print("✅ Ejercicios de ejemplo insertados")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    init_database()