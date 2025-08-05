
import db
from models.roles import Rol


def obtener_todos_roles():
    return db.session.query(Rol).all()

def obtener_rol_id(id_rol):
    return db.session.query(Rol).filter_by(id_rol=id_rol).first()

def crear_rol(nombre_rol,descripcion_rol):
    # Verificar si el rol existe
    rol_existente=db.session.query(Rol).filter_by(nombre_rol=nombre_rol).first()
    if rol_existente:
        raise ValueError(f"El Rol {nombre_rol} ya esta creado")

    # Crear el nuevo rol
    nuevo_rol=Rol(
        nombre_rol=nombre_rol,
        descripcion_rol=descripcion_rol
    )

    # Guardar en la base de datos
    db.session.add(nuevo_rol)
    db.session.commit()

    return nuevo_rol

def editar_rol(id_rol,nombre_rol, descripcion_rol):
    rol=obtener_rol_id(id_rol)
    if not rol:
        raise ValueError(f"El Rol {id_rol} no existe")

    rol.nombre_rol=nombre_rol
    rol.descripcion_rol=descripcion_rol

    db.session.commit()

    return rol

def eliminar_rol(id_rol):
    rol=obtener_rol_id(id_rol)
    if not rol:
        raise ValueError(f"El Rol {id_rol} no existe")
    else:
        db.session.delete(rol)
        db.session.commit()
        return rol