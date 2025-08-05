
from models.torneos import Torneo
import db

def obtener_torneos():
    return db.session.query(Torneo).all()


def obtener_torneo_id(id_torneo):
    return db.session.query(Torneo).get(id_torneo)

def crear_torneo(nombre_torneo,fecha_inicio_torneo,fecha_final_torneo,tipo_torneo,estado_torneo):
    torneo_existente=db.session.query(Torneo).filter_by(nombre_torneo=nombre_torneo).first()
    if torneo_existente:
        raise ValueError(f'El torneo "{nombre_torneo}" ya existe, intenta con otro')

    nuevo_torneo=Torneo(
        nombre_torneo=nombre_torneo,
        fecha_inicio_torneo=fecha_inicio_torneo,
        fecha_final_torneo=fecha_final_torneo,
        tipo_torneo=tipo_torneo,
        estado_torneo=estado_torneo,
    )

    db.session.add(nuevo_torneo)
    db.session.commit()

    return nuevo_torneo

def editar_torneo(id_torneo,nombre_torneo,fecha_inicio_torneo,fecha_final_torneo,tipo_torneo,estado_torneo):
    torneo=obtener_torneo_id(id_torneo)
    if not torneo:
        raise ValueError(f'El torneo "{id_torneo}" no existe')

    # Verificar si el nombre del torneo ya está asignado a OTRO torneo
    # Solo verificar si el nombre está cambiando
    if nombre_torneo != torneo.nombre_torneo:
        torneo_existente = db.session.query(Torneo).filter(
            Torneo.nombre_torneo == nombre_torneo,
            Torneo.id_torneo != id_torneo  # Excluir el torneo actual
        ).first()

        if torneo_existente:
            raise ValueError(f"El torneo {nombre_torneo} ya existe, intenta con otro")


    # Actualizar datos
    torneo.nombre_torneo=nombre_torneo
    torneo.fecha_inicio_torneo=fecha_inicio_torneo
    torneo.fecha_final_torneo=fecha_final_torneo
    torneo.tipo_torneo=tipo_torneo
    torneo.estado_torneo=estado_torneo

    # Guardar cambios
    db.session.add(torneo)
    db.session.commit()

    return torneo

