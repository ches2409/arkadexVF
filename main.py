from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload

from db import init_db
from enums.tipos import RolUsuario, TipoTorneo, EstadoTorneo
from models import roles, usuarios, torneos, juegos, equipos

import db
from models.roles import Rol
from models.torneos import Torneo
from models.usuarios import Usuario

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    todos_los_roles=db.session.query(Rol).all()
    usuarios_con_roles=db.session.query(Usuario).options(joinedload(Usuario.roles)).all()
    todos_los_torneos=db.session.query(Torneo).all()

    return render_template('index.html', roles=todos_los_roles, usuarios=usuarios_con_roles, roles_enum=RolUsuario, tipo_torneos_enum=TipoTorneo, estado_torneos_enum=EstadoTorneo, torneos=todos_los_torneos)

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

@app.route('/editar-usuario/<id_usuario>', methods=['POST'])
def editar_usuario(id_usuario):
    usuario=db.session.query(Usuario).filter_by(id_usuario=id_usuario).first()
    if usuario is None:
        return redirect(url_for('home'))
    else:
        usuario.nombre_usuario=request.form["nombre_usuario"]
        usuario.email_usuario=request.form["campo_email"]
        usuario.password_usuario=request.form["campo_password"]
        db.session.commit()
        return redirect(url_for('home'))

@app.route('/eliminar-usuario/<id_usuario>')
def eliminar_usuario(id_usuario):
    db.session.query(Usuario).filter_by(id_usuario=int(id_usuario)).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/crear-torneo', methods=['POST'])
def crear_torneo():
    nombre_torneo = request.form["nombre_torneo"]
    fecha_inicio_torneo=datetime.strptime(request.form["fecha_inicio_torneo"], "%Y-%m-%d")
    fecha_final_torneo = request.form["fecha_fin_torneo"]
    fecha_final_torneo = datetime.strptime(fecha_final_torneo, "%Y-%m-%d") if fecha_final_torneo else None
    tipo_torneo=request.form["contenido_tipo_torneo"]
    estado_torneo=request.form["contenido_estado_torneo"]

    torneo=Torneo(nombre_torneo=nombre_torneo,fecha_inicio_torneo=fecha_inicio_torneo,fecha_final_torneo=fecha_final_torneo,tipo_torneo=tipo_torneo,estado_torneo=estado_torneo)

    db.session.add(torneo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/editar-torneo/<id_torneo>', methods=['POST'])
def editar_torneo(id_torneo):
    torneo=db.session.query(Torneo).get(id_torneo)
    if torneo is None:
        return redirect(url_for('home'))
    else:
        torneo.nombre_torneo=request.form["nombre_torneo"]
        torneo.fecha_inicio_torneo=datetime.strptime(request.form["fecha_inicio_torneo"],"%Y-%m-%d")
        fecha_final=request.form["fecha_fin_torneo"]
        torneo.fecha_final_torneo = datetime.strptime(fecha_final, "%Y-%m-%d") if fecha_final else None
        torneo.tipo_torneo=request.form["contenido_tipo_torneo"]
        torneo.estado_torneo=request.form["contenido_estado_torneo"]
        db.session.commit()
        return redirect(url_for('home'))

@app.route('/eliminar-torneo/<id_torneo>')
def eliminar_torneo(id_torneo):
    db.session.query(Torneo).filter_by(id_torneo=int(id_torneo)).delete()
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    init_db()
    app.run(debug=True)

