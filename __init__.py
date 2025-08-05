from flask import Flask

from routes.equipos import equipos_bp
from routes.inicio import inicio_bp
from routes.roles import roles_bp
from routes.usuarios import usuarios_bp
from routes.torneos import torneos_bp
from routes.juegos import juegos_bp
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        debug=True,
        SECRET_KEY='dev'
    )


    # Registrar Blueprint

    app.register_blueprint(inicio_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(torneos_bp)
    app.register_blueprint(juegos_bp)
    app.register_blueprint(equipos_bp)
    app.register_blueprint(auth_bp)