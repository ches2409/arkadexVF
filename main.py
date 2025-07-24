from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload

from db import init_db
from models import roles, usuarios, torneos, juegos, equipos

import db
from models.roles import Rol
from models.usuarios import Usuario

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    todos_los_roles=db.session.query(Rol).all()
    todos_los_usuarios=db.session.query(Usuario).all()
    usuarios_con_roles=db.session.query(Usuario).options(joinedload(Usuario.roles)).all()

    return render_template('index.html', roles=todos_los_roles, usuarios=usuarios_con_roles)

@app.route('/crear-rol', methods=['POST'])
def crear():
    nombre_rol = request.form["contenido_nombre"]
    desccripcion_rol = request.form["contenido_descripcion"]

    rol=Rol(nombre_rol=nombre_rol,descripcion_rol=desccripcion_rol)
    db.session.add(rol)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/editar-rol/<id_rol>', methods=['POST'])
def editar_rol(id_rol):
    # rol=db.session.query(Rol).get(id_rol)
    rol=db.session.query(Rol).filter_by(id_rol=id_rol).first()
    if rol is None:
        return redirect(url_for('home'))
    else:
        rol.nombre_rol=request.form["contenido_nombre"]
        rol.descripcion_rol=request.form["contenido_descripcion"]
    db.session.commit()
    return redirect(url_for('home'))
@app.route('/eliminar_rol/<id_rol>')
def eliminar(id_rol):
    db.session.query(Rol).filter_by(id_rol=int(id_rol)).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/crear-usuario', methods=['POST'])
def crear_usuario():
    nombre_usuario = request.form["nombre_usuario"]
    email_usuario = request.form["campo_email"]
    password_usuario = request.form["campo_password"]
    rol_usuario=request.form["id_rol"]

    usuario=Usuario(nombre_usuario=nombre_usuario,email_usuario=email_usuario,password_usuario=password_usuario,rol_id=rol_usuario)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

