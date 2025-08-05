from flask import Blueprint, render_template, request, redirect, url_for, flash

import db
from enums.paginas import PaginaSitio, RefPagina
from services import usuario_service

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/usuarios')
@usuarios_bp.route('/usuarios/<indice>')
def usuarios(indice=3):

    # Usar el servicio para obtener datos
    todos_los_roles = usuario_service.obtener_todos_roles()
    usuarios_con_roles = usuario_service.obtener_todos_usuario()
    return render_template('usuarios.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           referencia_enum=RefPagina,
                           roles=todos_los_roles,
                           usuarios=usuarios_con_roles
                           )

@usuarios_bp.route('/crear-usuario', methods=['POST'])
def crear_usuario():
    nombre_usuario = request.form["nombre_usuario"]
    email_usuario = request.form["campo_email"]
    password_usuario = request.form["campo_password"]
    rol_usuario=request.form["id_rol"]

    try:
        # Usar el servicio para crear el usuario
        usuario_service.crear_usuario(
            nombre_usuario=nombre_usuario,
            email_usuario=email_usuario,
            password_usuario=password_usuario,
            rol_id=rol_usuario
        )
        flash(f'Usuario {nombre_usuario} creado exitosamente', 'success')
    except ValueError as e:
        flash(f'Error al crear usuario: {str(e)}', 'danger')

    return redirect(url_for('usuarios.usuarios'))

@usuarios_bp.route('/editar-usuario/<id_usuario>', methods=['POST'])
def editar_usuario(id_usuario):

    nombre_usuario = request.form["nombre_usuario"]
    email_usuario = request.form["campo_email"]
    password_usuario = request.form["campo_password"]
    rol_usuario=request.form["id_rol"]

    try:

        # Usar el servicio para actualizar el usuario
        usuario_service.editar_usuario(
            id_usuario=id_usuario,
            nombre_usuario=nombre_usuario,
            email_usuario=email_usuario,
            password_usuario=password_usuario,
            rol_id=rol_usuario
        )
        flash('Usuario editado exitosamente', 'success')
    except ValueError as e:
        flash(f'Error al actualizar usuario:{str(e)}','danger')

    return redirect(url_for('usuarios.usuarios'))

@usuarios_bp.route('/eliminar-usuario/<id_usuario>')
def eliminar_usuario(id_usuario):
    try:

        usuario_service.eliminar_usuario(id_usuario)
        flash(f'Usuario eliminado correctamente', 'info')
    except ValueError as e:
        db.session.rollback()
        flash(f'Error al eliminar usuario:{str(e)}','danger')

    return redirect(url_for('usuarios.usuarios'))