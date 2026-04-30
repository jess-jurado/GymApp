from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from config import get_db_connection, SECRET_KEY
from routes.auth_utils import token_required
from functools import wraps
import jwt
import os
from datetime import datetime

rutinas_bp = Blueprint('rutinas', __name__)

def buscar_imagen_local(prefijo):
    if not prefijo:
        return None
    # Usamos una ruta relativa al directorio raíz del proyecto
    base_dir = os.path.join(os.getcwd(), 'Assets_gymApp', 'Imagenes')
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().startswith(prefijo.lower()) and file.split('.')[-1].lower() in ['jpg', 'jpeg', 'png', 'webp', 'gif']:
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                rel_path = rel_path.replace('\\', '/')
                return f"/imagenes/{rel_path}"
    return None

@rutinas_bp.route('/dashboard')
@token_required
def dashboard(current_user):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Obtener nombre del usuario si no está en sesión
    nombre_usuario = session.get('user_nombre')
    if not nombre_usuario:
        cursor.execute("SELECT Nombre FROM Usuarios WHERE Id = ?", (current_user,))
        res = cursor.fetchone()
        nombre_usuario = res[0] if res else "Usuario"
        session['user_nombre'] = nombre_usuario

    # Lógica de entrenamiento de hoy
    dias_map = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves", 4: "Viernes", 5: "Sábado", 6: "Domingo"}
    dia_actual_nombre = dias_map[datetime.now().weekday()]
    
    cursor.execute("""
        SELECT e.id, e.Nombre_ejercicio, e.Subgrupo_muscular, r.id as r_id, r.Nombre_rutina
        FROM Rutinas r
        JOIN Ejercicios e ON r.Id_ejercicio = e.id
        WHERE r.Usuario_id = ? AND r.Dia = ?
    """, (current_user, dia_actual_nombre))
    ejercicios_hoy_rows = cursor.fetchall()

    inicio_hoy = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    cursor.execute("SELECT DISTINCT Id_ejercicio FROM Historial WHERE Usuario_id = ? AND Fecha >= ?", (current_user, inicio_hoy))
    completados_ids = {row[0] for row in cursor.fetchall()}

    ejercicios_hoy = []
    total_hoy = len(ejercicios_hoy_rows)
    realizados_hoy = 0

    for eid, nombre_ej, subgrupo, rid, n_rutina in ejercicios_hoy_rows:
        esta_hecho = eid in completados_ids
        if esta_hecho: realizados_hoy += 1
        ejercicios_hoy.append({
            "id": eid, "nombre": nombre_ej, "subgrupo": subgrupo,
            "completado": esta_hecho, "rutina_nombre": n_rutina, "r_id": rid
        })

    porcentaje_hoy = int((realizados_hoy / total_hoy * 100)) if total_hoy > 0 else 0

    cursor.execute("SELECT id, Nombre_rutina FROM Rutinas WHERE Usuario_id = ?", (current_user,))
    rows = cursor.fetchall()
    rutinas = []
    nombres_unicos = set()
    for r_id, n_rutina in rows:
        if n_rutina not in nombres_unicos:
            nombres_unicos.add(n_rutina)
            rutinas.append({"id": r_id, "nombre_rutina": n_rutina})

    cursor.close()
    conn.close()

    return render_template('dashboard.html', 
                           rutinas=rutinas, nombre=nombre_usuario,
                           dia_nombre=dia_actual_nombre, ejercicios_hoy=ejercicios_hoy,
                           porcentaje_hoy=porcentaje_hoy)

@rutinas_bp.route('/detalle_rutina/<int:id>')
@token_required
def detalle_rutina(current_user, id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, Nombre_rutina, Usuario_id FROM Rutinas WHERE id = ?", (id,))
    rutina = cursor.fetchone()

    if not rutina:
        flash("Rutina no encontrada.", "error")
        return redirect(url_for("rutinas.dashboard"))

    nombre_rutina = rutina[1]
    cursor.execute("""
        SELECT r.Dia, e.id, e.Nombre_ejercicio, e.Subgrupo_muscular, r.id
        FROM Rutinas r
        INNER JOIN Ejercicios e ON r.Id_ejercicio = e.id
        WHERE r.Nombre_rutina = ? AND r.Usuario_id = ?
    """, (nombre_rutina, current_user))
    ejercicios = cursor.fetchall()

    inicio_hoy = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    cursor.execute("SELECT DISTINCT Id_ejercicio FROM Historial WHERE Usuario_id = ? AND Fecha >= ?", (current_user, inicio_hoy))
    completados_hoy = {row[0] for row in cursor.fetchall()}

    ejercicios_por_dia = {}
    orden_dias = {"Lunes": 1, "Martes": 2, "Miércoles": 3, "Jueves": 4, "Viernes": 5, "Sábado": 6, "Domingo": 7}
    for dia, e_id, e_nom, sub, r_id in ejercicios:
        if dia not in ejercicios_por_dia: ejercicios_por_dia[dia] = []
        ejercicios_por_dia[dia].append({"id": e_id, "Nombre_ejercicio": e_nom, "Subgrupo_muscular": sub, "r_id": r_id})

    ejercicios_por_dia_ordenado = dict(sorted(ejercicios_por_dia.items(), key=lambda x: orden_dias.get(x[0], 999)))

    cursor.close()
    conn.close()

    return render_template('detalle_rutina.html', 
                           rutina={"id": id, "Nombre_rutina": nombre_rutina},
                           ejercicios_por_dia=ejercicios_por_dia_ordenado,
                           completados_hoy=completados_hoy)

@rutinas_bp.route('/detalle_ejercicio/<int:rutina_id>/<int:ejercicio_id>')
@token_required
def detalle_ejercicio(current_user, rutina_id, ejercicio_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, Nombre_ejercicio, Subgrupo_muscular, imagen_url, Grupo_muscular FROM Ejercicios WHERE id = ?", (ejercicio_id,))
    ejercicio = cursor.fetchone()

    if not ejercicio:
        flash("Ejercicio no encontrado.", "error")
        return redirect(url_for('rutinas.dashboard'))

    imagen_url = buscar_imagen_local(ejercicio[3]) if ejercicio[3] else None
    is_cardio = (ejercicio[4] == 'Cardio')

    cursor.close()
    conn.close()

    return render_template('detalle_ejercicio.html', 
                           nombre_ejercicio=ejercicio[1], subgrupo_muscular=ejercicio[2],
                           imagen_url=imagen_url, ejercicio_id=ejercicio_id, is_cardio=is_cardio)

@rutinas_bp.route("/crear_rutina", methods=["GET"])
@token_required
def mostrar_formulario_crear_rutina(current_user):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, Nombre_ejercicio FROM Ejercicios")
    ejercicios = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("crear_rutina.html", ejercicios=ejercicios)

@rutinas_bp.route('/get_subgrupos', methods=['GET'])
def get_subgrupos():
    grupo = request.args.get('grupo')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Subgrupo_muscular FROM Ejercicios WHERE Grupo_muscular = ?", (grupo,))
    subgrupos = cursor.fetchall()
    conn.close()
    return jsonify({'subgrupos': [s[0] for s in subgrupos]})

@rutinas_bp.route('/get_ejercicios', methods=['GET'])
def get_ejercicios():
    grupo = request.args.get('grupo')
    subgrupo = request.args.get('subgrupo')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, Nombre_ejercicio, imagen_url, Subgrupo_muscular FROM Ejercicios WHERE Grupo_muscular = ? AND Subgrupo_muscular = ?", (grupo, subgrupo))
    rows = cursor.fetchall()
    ejercicios = []
    for row in rows:
        ejercicios.append({
            'id': row[0], 'Nombre_ejercicio': row[1],
            'imagen_url': buscar_imagen_local(row[2]), 'Subgrupo_muscular': row[3]
        })
    conn.close()
    return jsonify({"ejercicios": ejercicios})

@rutinas_bp.route("/rutinas", methods=["POST"])
@token_required
def crear_rutina(current_user):
    data = request.json
    nombre_rutina = data.get("nombre_rutina")
    dias = data.get("dias")
    if not nombre_rutina or not dias:
        return jsonify({"error": "Faltan datos"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        for dia, grupos in dias.items():
            for grupo_info in grupos:
                for ej_id in grupo_info.get("ejercicios", []):
                    cursor.execute("INSERT INTO Rutinas (Usuario_id, Nombre_rutina, Id_ejercicio, Dia) VALUES (?, ?, ?, ?)",
                                 (current_user, nombre_rutina, ej_id, dia))
        conn.commit()
        return jsonify({"mensaje": "Rutina creada exitosamente"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
