from datetime import datetime
from flask import Flask, render_template

from db import init_db
from routes.equipos import equipos, equipos_bp

from routes.inicio import inicio_bp
from routes.roles import roles_bp
from routes.usuarios import usuarios_bp
from routes.torneos import torneos_bp
from routes.juegos import juegos_bp

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(inicio_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(torneos_bp)
app.register_blueprint(juegos_bp)
app.register_blueprint(equipos_bp)

# Context processors
@app.context_processor
def date_now():
    return  {
        'now':datetime.utcnow()
    }
# def utility_processor():
#     def get_route_for_page(page_name):
#         routes={
#             'inicio': 'inicio.inicio',
#             'roles': 'roles.roles',
#             'usuarios': 'usuarios.usuarios',
#             'torneos': 'torneos.torneos',
#             'juegos': 'juegos.juegos',
#         }
#         return routes.get(page_name, page_name)
#     return dict(get_route_for_page=get_route_for_page)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

