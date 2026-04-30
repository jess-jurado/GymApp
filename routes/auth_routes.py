from flask import Blueprint, request, jsonify, session, redirect, url_for, flash
import bcrypt
import jwt
import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import get_db_connection, SECRET_KEY
from routes.auth_utils import token_required

auth_bp = Blueprint("auth", __name__)

# Configuración SMTP desde .env
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

def send_confirmation_email(recipient, token):
    """
    Envía un correo de confirmación si las credenciales están configuradas.
    """
    if not SMTP_USER or not SMTP_PASS:
        print("⚠️ SMTP no configurado. El correo de confirmación no se enviará.")
        return False

    confirm_link = f"http://tu-dominio.com/confirmar/{token}" # Cambiar por tu URL real
    
    subject = "Confirma tu cuenta en GymBRoot"
    body = f"""
    <html>
    <body>
        <h2>¡Bienvenido a GymBRoot!</h2>
        <p>Para activar tu cuenta y empezar a entrenar, haz clic en el siguiente enlace:</p>
        <a href="{confirm_link}" style="padding: 10px 20px; background: #38bdf8; color: white; text-decoration: none; border-radius: 5px;">Confirmar Cuenta</a>
    </body>
    </html>
    """

    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, recipient, msg.as_string())
            return True
    except Exception as e:
        print(f"❌ Error enviando correo: {e}")
        return False

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if session.get('user_id'):
        return redirect(url_for('rutinas.dashboard'))
        
    if request.method == "POST":
        # Manejo de formulario (web) o JSON (API)
        data = request.json if request.is_json else request.form
        nombre = data.get("nombre")
        email = data.get("email")
        password = data.get("password")

        if not nombre or not email or not password:
            return jsonify({"error": "Faltan datos"}), 400

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM Usuarios WHERE Email = ?", (email,))
            if cursor.fetchone():
                return jsonify({"error": "El correo ya está registrado"}), 400

            cursor.execute(
                "INSERT INTO Usuarios (Nombre, Email, Password_hash, Confirmado) VALUES (?, ?, ?, ?)",
                (nombre, email, hashed_password, 0),
            )
            conn.commit()

            # Lógica opcional de token para email si se desea activar
            # token = jwt.encode({"email": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY)
            # send_confirmation_email(email, token)

            if request.is_json:
                return jsonify({"mensaje": "Registro exitoso"}), 201
            
            flash("Registro exitoso. Ya puedes iniciar sesión.", "success")
            return redirect(url_for("auth.login"))

        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get('user_id'):
        return redirect(url_for('rutinas.dashboard'))

    if request.method == "POST":
        data = request.json if request.is_json else request.form
        email = data.get("email")
        password = data.get("password")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Id, Password_hash, Nombre FROM Usuarios WHERE Email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(password.encode("utf-8"), user[1].encode("utf-8")):
            session['user_id'] = user[0]
            session['user_nombre'] = user[2]
            
            token = jwt.encode(
                {"user_id": user[0], "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)},
                SECRET_KEY, algorithm="HS256"
            )

            if request.is_json:
                return jsonify({"token": token, "mensaje": "Login exitoso"})
            
            flash("Inicio de sesión exitoso.", "success")
            return redirect(url_for("rutinas.dashboard"))
        
        if request.is_json:
            return jsonify({"error": "Credenciales incorrectas"}), 401
        
        flash("Correo o contraseña incorrectos.", "error")
        return redirect(url_for("auth.login"))

    return render_template("login.html")

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.", "success")
    return redirect(url_for('auth.login'))

@auth_bp.route("/confirmar/<token>", methods=["GET"])
def confirmar_cuenta(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email = decoded.get("email")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Usuarios SET Confirmado = 1 WHERE Email = ?", (email,))
        conn.commit()
        conn.close()

        flash("Cuenta confirmada correctamente.", "success")
        return redirect(url_for("auth.login"))
    except:
        flash("Token inválido o expirado.", "error")
        return redirect(url_for("auth.login"))