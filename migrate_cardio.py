from config import get_db_connection

def migrate():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Añadir columna Calorias a Historial
        try:
            cursor.execute("ALTER TABLE Historial ADD COLUMN Calorias INTEGER")
            print("✅ Columna 'Calorias' añadida a Historial")
        except Exception as e:
            print(f"ℹ️  Calorias ya existe o error: {e}")

        # Añadir columna Duracion_min a Historial
        try:
            cursor.execute("ALTER TABLE Historial ADD COLUMN Duracion_min INTEGER")
            print("✅ Columna 'Duracion_min' añadida a Historial")
        except Exception as e:
            print(f"ℹ️  Duracion_min ya existe o error: {e}")

        # Insertar ejercicios de cardio si no existen
        cardio_exercises = [
            ('Cinta de Correr', 'Cardio', 'Cardio', None),
            ('Eliptica',        'Cardio', 'Cardio', None),
        ]

        for nombre, grupo, subgrupo, imagen in cardio_exercises:
            cursor.execute("SELECT id FROM Ejercicios WHERE Nombre_ejercicio = ?", (nombre,))
            if not cursor.fetchone():
                cursor.execute(
                    "INSERT INTO Ejercicios (Nombre_ejercicio, Grupo_muscular, Subgrupo_muscular, imagen_url) VALUES (?, ?, ?, ?)",
                    (nombre, grupo, subgrupo, imagen)
                )
                print(f"✅ Ejercicio '{nombre}' insertado")
            else:
                print(f"ℹ️  '{nombre}' ya existe, omitiendo")

        conn.commit()
        print("✅ Migración de cardio completada correctamente")

    except Exception as e:
        print(f"❌ Error durante la migración: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    migrate()
