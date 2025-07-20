from flask import Flask, render_template, request
from sqlalchemy.orm import joinedload

from db import init_db
from models import roles, usuarios

import db
from models.roles import Rol
from models.usuarios import Usuario

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    todos_los_roles=db.session.query(Rol).all()
    todos_los_usuarios=db.session.query(Usuario).all()
    usuarios_con_roles=db.session.query(Usuario).options(joinedload(Usuario.roles)).all()
    print(todos_los_usuarios)
    return render_template('index.html', roles=todos_los_roles, usuarios=usuarios_con_roles)

@app.route('/crear-rol', methods=['POST'])
def crear():
    nombre_rol = request.form["contenido_prueba"]
    desccripcion_rol = request.form["contenido_des"]

    rol=Rol(nombre_rol=nombre_rol,descripcion_rol=desccripcion_rol)
    db.session.add(rol)
    db.session.commit()

    return "Rol creado con exito"

@app.route('/crear-usuario', methods=['POST'])
def crear_usuario():
    nombre_usuario = request.form["nombre_usuario"]
    email_usuario = request.form["campo_email"]
    password_usuario = request.form["campo_password"]
    rol_usuario=request.form["id_rol"]


    usuario=Usuario(nombre_usuario=nombre_usuario,email_usuario=email_usuario,password_usuario=password_usuario,rol_id=rol_usuario)
    db.session.add(usuario)
    db.session.commit()
    return "Usuario creado con exito"


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

