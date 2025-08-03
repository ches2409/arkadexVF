from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload

import db
from models.roles import Rol
from models.usuarios import Usuario
from enums.paginas import PaginaSitio, RefPagina

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/usuarios')
@usuarios_bp.route('/usuarios/<indice>')
def usuarios(indice=3):
    todos_los_roles = db.session.query(Rol).all()
    usuarios_con_roles = db.session.query(Usuario).options(joinedload(Usuario.roles)).all()
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

    usuario=Usuario(nombre_usuario=nombre_usuario,email_usuario=email_usuario,password_usuario=password_usuario,rol_id=rol_usuario)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('usuarios.usuarios'))

@usuarios_bp.route('/editar-usuario/<id_usuario>', methods=['POST'])
def editar_usuario(id_usuario):
    usuario=db.session.query(Usuario).filter_by(id_usuario=id_usuario).first()
    if usuario is None:
        return redirect(url_for('usuarios.usuarios'))
    else:
        usuario.nombre_usuario=request.form["nombre_usuario"]
        usuario.email_usuario=request.form["campo_email"]
        usuario.password_usuario=request.form["campo_password"]
        db.session.commit()
        return redirect(url_for('usuarios.usuarios'))

@usuarios_bp.route('/eliminar-usuario/<id_usuario>')
def eliminar_usuario(id_usuario):
    db.session.query(Usuario).filter_by(id_usuario=int(id_usuario)).delete()
    db.session.commit()
    return redirect(url_for('usuarios.usuarios'))