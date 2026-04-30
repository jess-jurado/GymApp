from flask import Blueprint, request, jsonify, session, render_template
from config import get_db_connection
from routes.auth_utils import token_required
from datetime import datetime
import os

workout_bp = Blueprint('workout', __name__)

def buscar_imagen_local(prefijo):
    if not prefijo: return None
    base_dir = os.path.join(os.getcwd(), 'Assets_gymApp', 'Imagenes')
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().startswith(prefijo.lower()):
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                rel_path = rel_path.replace('\\', '/')
                return f"/imagenes/{rel_path}"
    return None

@workout_bp.route('/guardar_cardio/<int:ejercicio_id>', methods=['POST'])
@token_required
def guardar_cardio(current_user, ejercicio_id):
    data = request.get_json(force=True)
    duracion = data.get('duracion')
    calorias = data.get('calorias')
    if duracion is None or calorias is None:
        return jsonify({"error": "Datos incompletos"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
        INSERT INTO Historial (Id_ejercicio, Series, Repeticiones, Peso, Fecha, Usuario_id, Calorias, Duracion_min)
        VALUES (?, 1, 0, 0, ?, ?, ?, ?)
    """, (ejercicio_id, fecha_actual, current_user, calorias, duracion))
    conn.commit()
    conn.close()
    return jsonify({"message": "Cardio guardado correctamente"}), 200

@workout_bp.route('/guardar_series/<int:ejercicio_id>', methods=['POST'])
@token_required
def guardar_series(current_user, ejercicio_id):
    data = request.get_json(force=True)
    series = data.get('series', [])
    if not series:
        return jsonify({"error": "No se enviaron datos"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for s in series:
        cursor.execute("""
            INSERT INTO Historial (Id_ejercicio, Series, Repeticiones, Peso, Fecha, Usuario_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (ejercicio_id, s['serie'], s['repeticiones'], s['peso'], fecha_actual, current_user))
    conn.commit()
    conn.close()
    return jsonify({"message": "Datos guardados correctamente"}), 200

@workout_bp.route('/api/obtener_fechas_entrenamiento', methods=['GET'])
@token_required
def obtener_fechas_entrenamiento(current_user):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Fecha FROM Historial WHERE Usuario_id = ? ORDER BY Fecha ASC", (current_user,))
    fechas = [row[0].split(" ")[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify({"fechas": fechas})

@workout_bp.route('/api/obtener_series/<int:ejercicio_id>/<fecha>', methods=['GET'])
@token_required
def obtener_series(current_user, ejercicio_id, fecha):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Series, Repeticiones, Peso FROM Historial
        WHERE Id_ejercicio = ? AND Fecha LIKE ? AND Usuario_id = ?
        ORDER BY Series ASC
    """, (ejercicio_id, f"{fecha}%", current_user))
    rows = cursor.fetchall()
    conn.close()
    return jsonify({"series": [{"serie": r[0], "repeticiones": r[1], "peso": r[2]} for r in rows]})

@workout_bp.route('/entrenamientos_realizados/<fecha>', methods=['GET'])
@token_required
def entrenamientos_realizados(current_user, fecha):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT e.id, e.Nombre_ejercicio, e.Subgrupo_muscular, e.Grupo_muscular, e.imagen_url
        FROM Historial h JOIN Ejercicios e ON h.Id_ejercicio = e.id
        WHERE h.Fecha LIKE ? AND h.Usuario_id = ?
    """, (f"{fecha}%", current_user))
    ejercicios = [{"id": r[0], "nombre": r[1], "subgrupo": r[2], "grupo": r[3], "imagen": buscar_imagen_local(r[4])} for r in cursor.fetchall()]
    conn.close()
    return render_template("entrenamientos_realizados.html", ejercicios=ejercicios, fecha=fecha)
