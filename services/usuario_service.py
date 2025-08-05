from models.usuarios import Usuario
from models.roles import Rol
from sqlalchemy.orm import joinedload
import db

def obtener_todos_usuario():
    """
    Obtiene todos los usuarios con sus roles relacionados.

    Returns:
        list: Lista de objetos Usuario con sus roles cargados
    """
    return db.session.query(Usuario).options(joinedload(Usuario.roles)).all()

def obtener_usuario_id(id_usuario):
    """
    Obtiene un usuario por su ID.

    Args:
        id_usuario (int): ID del usuario a buscar

    :returns:
        Usuario: Objeto usuario si existe, None en caso contrario
    """
    return db.session.query(Usuario).filter_by(id_usuario=id_usuario).first()

def obtener_todos_roles():
    """
    Obtiene todos los roles relacionados.

    Return:
        list: lista de objetos Rol
    """
    # db.session.query(Usuario).options(joinedload(Usuario.roles)).all()
    return db.session.query(Rol).all()

def crear_usuario(nombre_usuario, email_usuario, password_usuario,rol_id):
    """
    Crea un nuevo usuario en la base de datos.

    Args:
        nombre_usuario (str): Nombre del usuario
        email_usuario (str): Email del usuario
        password_usuario (str): Contraseña del usuario
        rol_id (int): ID del rol asignado al usuario

    Returns:
        Usuario: El usuario creado

    Raises:
        ValueError: Si el email ya existe en la base de datos
    """
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

def editar_usuario(id_usuario, nombre_usuario, email_usuario, password_usuario,rol_id):
    """
    Actualiza los datos de un usuario existente.

    Args:
        id_usuario (int): ID del usuario a actualizar
        nombre_usuario (str): Nuevo nombre del usuario
        email_usuario (str): Nuevo email del usuario
        password_usuario (str): Nueva contraseña del usuario
        rol_id (int): ID del rol asignado al usuario

    Returns:
        Usuario: El usuario actualizado

    Raises:
        ValueError: Si el usuario no existe o si el email ya está en uso por otro usuario
    """
    # Obtener el usuario
    usuario=obtener_usuario_id(id_usuario)
    if not usuario:
        raise ValueError(f'No existe un usuario con ID {id_usuario}')

    # Verificar si el email ya existe y no pertenece a este usuario
    if email_usuario != usuario.email_usuario:
        usuario_existente=db.session.query(Usuario).filter_by(email_usuario=email_usuario).first()
        if usuario_existente:
            raise ValueError(f'El email {email_usuario} ya esta registrado por otro usuario')

    # Actualizar los datos
    usuario.nombre_usuario = nombre_usuario
    usuario.email_usuario = email_usuario
    usuario.password_usuario = password_usuario
    usuario.rol_id = rol_id

    #Guardar cambios
    db.session.commit()

    return usuario

def eliminar_usuario(id_usuario):
    usuario=obtener_usuario_id(id_usuario)
    if not usuario:
        raise ValueError(f'usuario no encontrado')
    else:
        # nombre=usuario.nombre_usuario
        db.session.delete(usuario)
        db.session.commit()
        return usuario