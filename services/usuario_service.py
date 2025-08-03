from models.usuarios import Usuario
from models.roles import Rol
from sqlalchemy.orm import joinedload
import db

def obtener_usuario():
    return db.session.query(Usuario).all()

def obtener_usuario_id(id_usuario):
    return db.session.query(Usuario).filter_by(id_usuario=id_usuario).first()

def crear_usuario(nombre_usuario, email_usuario, password_usuario,rol_id):
    # Verificar el e-mail existente
    usuario_existente=db.session.query(Usuario).filter_by(email_usuario=email_usuario).first()
    if usuario_existente:
        raise ValueError(f'El email {email_usuario} ya esta registrado')

    # Crear el nuevo usuario
    nuevo_usuario = Usuario(
        nombre_usuario=nombre_usuario,
        email_usuario=email_usuario,
        password_usuario=password_usuario,
        rol_id=rol_id
    )

    # Guardar en la Base de Datos
    db.session.add(nuevo_usuario)
    db.session.commit()

    return nuevo_usuario

