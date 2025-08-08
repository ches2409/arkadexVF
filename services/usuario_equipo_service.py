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
        Torneo.nombre_torneo,
        UsuarioEquipo.rol_equipo
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

def afiliar_usuario_equipo(
    usuario_id: int,
    equipo_id: int,
    torneo_id: int,
    rol_equipo: str
):
    # Verificar si la afiliación ya existe
    afiliacion_existente = db.session.query(UsuarioEquipo).filter_by(
        usuario_id=usuario_id,
        equipo_id=equipo_id,
        torneo_id=torneo_id
    ).first()

    if afiliacion_existente:
        raise ValueError("El usuario ya está afiliado a este equipo en el torneo")

    # Crear nueva afiliación
    nueva_afiliacion = UsuarioEquipo(
        usuario_id=usuario_id,
        equipo_id=equipo_id,
        torneo_id=torneo_id,
        rol_equipo=rol_equipo
    )

    db.session.add(nueva_afiliacion)
    db.session.commit()

    return nueva_afiliacion