import jwt
import datetime
from flask import jsonify, request, session
from functools import wraps
from config import SECRET_KEY

def encode_auth_token(user_id):
    """
    Genera un token JWT para un usuario.
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'user_id': user_id
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    except Exception as e:
        return None

def token_required(f):
    """
    Decorador unificado para proteger rutas.
    Soporta JWT (Header Authorization) y fallback a Sesión Flask.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        token = auth_header[7:].strip() if auth_header.startswith("Bearer ") else ''
        
        current_user = None

        if token:
            try:
                decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                current_user = decoded['user_id']
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                # Si el token falla, intentamos sesión antes de rechazar
                current_user = session.get("user_id")
        else:
            # Sin token → usar sesión Flask
            current_user = session.get("user_id")

        if not current_user:
            return jsonify({"error": "No autorizado. Por favor inicia sesión."}), 401

        return f(current_user, *args, **kwargs)
    
    return decorated_function
