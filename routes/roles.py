from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import joinedload

import db
from models.roles import Rol
from models.usuarios import Usuario
from enums.tipos import RolUsuario
from enums.paginas import PaginaSitio, RefPagina
from services import rol_service

# Crear el blueprint
roles_bp = Blueprint('roles', __name__)

# Pagina de carga de roles
@roles_bp.route('/roles')
@roles_bp.route('/roles/<indice>')
def roles(indice=2):
    todos_los_roles = db.session.query(Rol).all()
    usuarios_con_roles = db.session.query(Usuario).options(joinedload(Usuario.roles)).all()
    todos_los_roles = db.session.query(Rol).all()
    return render_template('roles.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           referencia_enum=RefPagina,
                           roles=todos_los_roles,
                           roles_enum=RolUsuario
                           )

# Crear un nuevo rol
@roles_bp.route('/crear-rol', methods=['POST'])
def crear():
    nombre_rol = request.form["contenido_nombre"]
    desccripcion_rol = request.form["contenido_descripcion"]

    try:
        rol_service.crear_rol(
            nombre_rol=nombre_rol,
            descripcion_rol=desccripcion_rol
        )
        flash(f'Rol: {nombre_rol}, se ha creado exitosamente', 'success')
    except ValueError as e:
        flash(f'Error al crear rol: {str(e)}', 'danger')

    return redirect(url_for('roles.roles'))

# Editar un rol
@roles_bp.route('/editar-rol/<id_rol>', methods=['POST'])
def editar_rol(id_rol):
    nombre_rol = request.form["contenido_nombre"]
    desccripcion_rol = request.form["contenido_descripcion"]

    try:
        rol_service.editar_rol(id_rol=id_rol,
                               nombre_rol=nombre_rol,
                               descripcion_rol=desccripcion_rol
                               )
        flash(f"El Rol ha sido actualizado con exito", 'success')
    except ValueError as e:
        flash(f'Error al crear el rol:{str(e)}', 'danger')
    return redirect(url_for('roles.roles'))

# Eliminar un rol
@roles_bp.route('/eliminar_rol/<id_rol>')
def eliminar(id_rol):

    try:

        rol_service.eliminar_rol(id_rol=id_rol)
        flash(f'rol eliminado correctamente', 'info')
    except ValueError as e:
        db.session.rollback()
        flash(f'Error al eliminar usuario:{str(e)}','danger')

    return redirect(url_for('roles.roles'))
