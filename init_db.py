from config import get_db_connection

def init_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        print("🔄 Creando tablas en PostgreSQL...")
        
        # Tabla Usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Usuarios (
                Id SERIAL PRIMARY KEY,
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
                id SERIAL PRIMARY KEY,
                Nombre_ejercicio VARCHAR(100) UNIQUE NOT NULL,
                Grupo_muscular VARCHAR(50),
                Subgrupo_muscular VARCHAR(50),
                imagen_url VARCHAR(255)
            )
        ''')
        
        # Tabla Rutinas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Rutinas (
                id SERIAL PRIMARY KEY,
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
                id SERIAL PRIMARY KEY,
                Id_ejercicio INTEGER REFERENCES Ejercicios(id),
                Series INTEGER,
                Repeticiones INTEGER,
                Peso DECIMAL(10,2),
                Fecha TIMESTAMP,
                Usuario_id INTEGER REFERENCES Usuarios(Id)
            )
        ''')
        
        # Tabla Series
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Series (
                id SERIAL PRIMARY KEY,
                Entrenamiento_id INTEGER,
                Peso DECIMAL(10,2),
                Repeticiones INTEGER,
                Fecha DATE,
                Id_ejercicio INTEGER REFERENCES Ejercicios(id)
            )
        ''')
        
        # Ejercicios de ejemplo
        ejercicios = [
            ('Press de banca', 'Pecho', 'Pectoral superior', 'press_banca'),
            ('Sentadillas', 'Piernas', 'Cuádriceps', 'sentadillas'),
            ('Curl de bíceps', 'Brazo', 'Bíceps', 'curl_biceps'),
            ('Dominadas', 'Espalda', 'Dorsales', 'dominadas'),
            ('Press militar', 'Hombro', 'Deltoides frontal', 'press_militar'),
            ('Peso muerto', 'Espalda', 'Espalda baja', 'peso_muerto'),
            ('Fondos en paralelas', 'Pecho', 'Pectoral inferior', 'fondos'),
            ('Elevaciones laterales', 'Hombro', 'Deltoides lateral', 'elevaciones_laterales')
        ]
        
        print("🔄 Insertando ejercicios...")
        for ejercicio in ejercicios:
            try:
                cursor.execute('''
                    INSERT INTO Ejercicios (Nombre_ejercicio, Grupo_muscular, Subgrupo_muscular, imagen_url)
                    VALUES (%s, %s, %s, %s)
                ''', ejercicio)
            except Exception as e:
                print(f"   ⚠️ Ejercicio '{ejercicio[0]}' ya existe, saltando...")
        
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