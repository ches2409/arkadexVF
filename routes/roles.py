from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload

import db
from models.roles import Rol
from models.usuarios import Usuario
from enums.tipos import RolUsuario
from enums.paginas import PaginaSitio

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
                           roles=todos_los_roles,
                           roles_enum=RolUsuario
                           )

# Crear un nuevo rol
@roles_bp.route('/crear-rol', methods=['POST'])
def crear():
    nombre_rol = request.form["contenido_nombre"]
    desccripcion_rol = request.form["contenido_descripcion"]

    rol=Rol(nombre_rol=nombre_rol,descripcion_rol=desccripcion_rol)
    db.session.add(rol)
    db.session.commit()

    return redirect(url_for('roles.roles'))

# Editar un rol
@roles_bp.route('/editar-rol/<id_rol>', methods=['POST'])
def editar_rol(id_rol):
    # rol=db.session.query(Rol).get(id_rol)
    rol=db.session.query(Rol).filter_by(id_rol=id_rol).first()
    if rol is None:
        return redirect(url_for('roles.roles'))
    else:
        rol.nombre_rol=request.form["contenido_nombre"]
        rol.descripcion_rol=request.form["contenido_descripcion"]
    db.session.commit()
    return redirect(url_for('roles.roles'))

# Eliminar un rol
@roles_bp.route('/eliminar_rol/<id_rol>')
def eliminar(id_rol):
    db.session.query(Rol).filter_by(id_rol=int(id_rol)).delete()
    db.session.commit()
    return redirect(url_for('roles.roles'))
