from flask import Blueprint, request, jsonify
from config import get_db_connection
from routes.auth_utils import token_required

user_bp = Blueprint('user', __name__)

@user_bp.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre, Email FROM Usuarios WHERE Id = ?", (current_user,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return jsonify({"nombre": user[0], "email": user[1]})
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404
