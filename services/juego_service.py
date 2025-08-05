from models.juegos import Juego
from models.torneos import Torneo
from sqlalchemy.orm import joinedload
import db

def obtener_todos_torneos():
    return db.session.query(Torneo).all()

def obtener_juegos_con_torneos():
    return db.session.query(Juego).options(joinedload(Juego.torneos)).all()

def obtener_juego_id(id_juego):
    return db.session.query(Juego).get(id_juego)


def crear_juego(nombre_juego,descripcion_juego,torneo_id):

    juego_existente=db.session.query(Juego).filter_by(nombre_juego=nombre_juego).first()
    if juego_existente:
        raise ValueError(f'El juego {nombre_juego} ya existe!')

    nuevo_juego=Juego(
        nombre_juego=nombre_juego,
        descripcion_juego=descripcion_juego,
        torneo_id=torneo_id
    )
    db.session.add(nuevo_juego)
    db.session.commit()
    return nuevo_juego

def editar_juego(id_juego, nombre_juego, descripcion_juego, torneo_id):
    juego=obtener_juego_id(id_juego)
    if not juego:
        raise ValueError(f'El juego {id_juego} no existe!')

    juego.nombre_juego=nombre_juego
    juego.descripcion_juego=descripcion_juego
    juego.torneo_id=torneo_id

    db.session.commit()
    return juego


def elimnar_juego(id_juego):
    juego=obtener_juego_id(id_juego)
    if not juego:
        raise ValueError(f'El juego {id_juego} no existe!')
    db.session.delete(juego)
    db.session.commit()
    return juego

