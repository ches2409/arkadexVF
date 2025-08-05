from datetime import datetime
from flask import Flask, render_template
import secrets

from db import init_db

from routes.equipos import equipos, equipos_bp
from routes.inicio import inicio_bp
from routes.roles import roles_bp
from routes.usuarios import usuarios_bp
from routes.torneos import torneos_bp
from routes.juegos import juegos_bp
from routes.auth import auth_bp
from routes.ejemplos_flash import ejemplos_flash_bp

app = Flask(__name__)

# Configuración de la clave secreta para sesiones y mensajes flash
app.secret_key = secrets.token_hex(16)

# Registrar los blueprints
app.register_blueprint(inicio_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(torneos_bp)
app.register_blueprint(juegos_bp)
app.register_blueprint(equipos_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(ejemplos_flash_bp)

# Context processors
@app.context_processor
def date_now():
    return  {
        'now':datetime.utcnow()
    }


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

