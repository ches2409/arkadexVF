from models.equipos import Equipo
import db


def obtener_todos_equipos():
    return db.session.query(Equipo).all()

def obtener_equipo(id_equipo):
    return db.session.query(Equipo).get(id_equipo)

def crear_equipo(nombre_equipo, descripcion_equipo, estado_equipo):
    equipo_existente=db.session.query(Equipo).filter_by(nombre_equipo=nombre_equipo).first()
    if equipo_existente:
        raise ValueError(f'El equipo {nombre_equipo} ya existe!')

    # Crear nuevo equipo
    nuevo_equipo=Equipo(
        nombre_equipo=nombre_equipo,
        descripcion_equipo=descripcion_equipo,
        estado_equipo=estado_equipo
    )

    # Guardar en la base de datos
    db.session.add(nuevo_equipo)
    db.session.commit()

    return nuevo_equipo

def editar_equipo(id_equipo, nombre_equipo, descripcion_equipo,estado_equipo):

    equipo=obtener_equipo(id_equipo)

    if not equipo:
        raise ValueError(f'El equipo {nombre_equipo} no existe!')

    if nombre_equipo != equipo.nombre_equipo:
        nommbre_distinto=db.session.query(Equipo).filter(
            Equipo.nombre_equipo==nombre_equipo,
            Equipo.id_equipo!=id_equipo
        ).first()
        if nommbre_distinto:
            raise ValueError(f'El equipo {nombre_equipo} ya existe!')

    # Actualizar datos
    equipo.nombre_equipo=nombre_equipo
    equipo.descripcion_equipo=descripcion_equipo
    equipo.estado_equipo=estado_equipo

    db.session.add(equipo)
    db.session.commit()

    return equipo

def eliminar_equipo(id_equipo):
    equipo=obtener_equipo(id_equipo)
    if not equipo:
        raise ValueError(f'El equipo {id_equipo} no existe!')

    db.session.delete(equipo)
    db.session.commit()
    return equipo

