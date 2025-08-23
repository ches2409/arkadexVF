from models.equipos import Equipo
from models.usuarios import Usuario
from models.torneos import Torneo
from models.usuarios_equipos import UsuarioEquipo

import db

def obtener_todos_equipos():
    return db.session.query(Equipo).all()

def obtener_todos_usuarios_equipos():
    return db.session.query(
        UsuarioEquipo,
        Usuario.nombre_usuario,
        Equipo.nombre_equipo,
        Torneo.nombre_torneo
    ).join(
        Usuario, UsuarioEquipo.usuario_id == Usuario.id_usuario
    ).join(
        Equipo, UsuarioEquipo.equipo_id == Equipo.id_equipo
    ).join(
        Torneo, UsuarioEquipo.torneo_id == Torneo.id_torneo
    ).all()
def obtener_todos_usuarios():
    return db.session.query(Usuario).all()
def obtener_todos_torneos():
    return db.session.query(Torneo).all()
