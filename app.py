from flask import Flask, render_template, send_from_directory, url_for
import os
import locale
from config import SECRET_KEY, get_db_connection

# Importación de Blueprints
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.workout_routes import workout_bp
from routes.rutina_routes import rutinas_bp
from routes.entrenamientos import entrenamientos_bp

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Configurar zona horaria Madrid para todo el servidor
os.environ['TZ'] = 'Europe/Madrid'
try:
    import time
    time.tzset()
except AttributeError:
    pass # Windows/Sistemas sin tzset

# Configurar localización en español
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES')
    except locale.Error:
        pass

# ── SERVIDOS DE ARCHIVOS ESTÁTICOS ──
@app.route('/imagenes/<path:filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'Assets_gymApp', 'Imagenes'), filename)

@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/sw.js')
def service_worker():
    return send_from_directory('static', 'sw.js')

# ── RUTAS PRINCIPALES ──
@app.route('/')
def index():
    return render_template("index.html")

# ── REGISTRO DE BLUEPRINTS ──
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(workout_bp)
app.register_blueprint(entrenamientos_bp, url_prefix='/api')
app.register_blueprint(rutinas_bp) # Quitamos el prefijo /api aquí para mantener compatibilidad con las URLs actuales

if __name__ == "__main__":
    # Puerto 5001 para evitar conflictos con otros servicios en local
    app.run(host='0.0.0.0', debug=True, port=5001)
