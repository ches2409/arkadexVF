from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload

from db import init_db
from enums.tipos import RolUsuario, TipoTorneo, EstadoTorneo
from enums.paginas import PaginaSitio
from models import roles, usuarios, torneos, juegos, equipos

import db
from models.juegos import Juego
from models.roles import Rol
from models.torneos import Torneo
from models.usuarios import Usuario

app = Flask(__name__)

# Context processors
@app.context_processor
def date_now():
    return  {
        'now':datetime.utcnow()
    }

@app.route('/roles')
@app.route('/roles/<indice>')
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
@app.route('/usuarios')
@app.route('/usuarios/<indice>')
def usuarios(indice=3):
    todos_los_roles = db.session.query(Rol).all()
    usuarios_con_roles = db.session.query(Usuario).options(joinedload(Usuario.roles)).all()
    return render_template('usuarios.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           roles=todos_los_roles,
                           usuarios=usuarios_con_roles
                           )
@app.route('/torneos')
@app.route('/torneos/<indice>')
def torneos(indice=4):
    todos_los_torneos = db.session.query(Torneo).all()
    return render_template('torneos.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           tipo_torneos_enum=TipoTorneo,
                           estado_torneos_enum=EstadoTorneo,
                           torneos=todos_los_torneos
                           )

@app.route('/juegos')
@app.route('/juegos/<indice>')
def juegos(indice=5):
    # indice=4
    todos_los_torneos = db.session.query(Torneo).all()
    juegos_con_torneos = db.session.query(Juego).options(joinedload(Juego.torneos)).all()
    return render_template('juegos.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           torneos=todos_los_torneos,
                           juegos=juegos_con_torneos
                           )


@app.route('/')
@app.route('/<indice>')
def inicio(indice=1):  # put application's code here

    return render_template('index.html',
                           indice=indice,
                           paginas_enum = PaginaSitio
                           )
    # todos_los_roles=db.session.query(Rol).all()
    # usuarios_con_roles=db.session.query(Usuario).options(joinedload(Usuario.roles)).all()
    # todos_los_torneos=db.session.query(Torneo).all()
    # juegos_con_torneos=db.session.query(Juego).options(joinedload(Juego.torneos)).all()
    #
    # return render_template('index.html', roles=todos_los_roles, usuarios=usuarios_con_roles, roles_enum=RolUsuario, tipo_torneos_enum=TipoTorneo, estado_torneos_enum=EstadoTorneo, torneos=todos_los_torneos, juegos=juegos_con_torneos)

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

@app.route('/crear-juego', methods=['POST'])
def crear_juego():
    nombre_juego = request.form["nombre_Juego"]
    descripcion_juego = request.form["descripcion_juego"]
    rol_torneo=request.form["id_torneo"]

    juego=Juego(nombre_juego=nombre_juego,descripcion_juego=descripcion_juego,torneo_id=rol_torneo)
    db.session.add(juego)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/editar-juego/<id_juego>', methods=['POST'])
def editar_juego(id_juego):
    juego=db.session.query(Juego).get(id_juego)
    if juego is None:
        return redirect(url_for('home'))
    else:
        juego.nombre_juego=request.form["nombre_juego"]
        juego.descripcion_juego=request.form["descripcion_juego"]
        juego.torneo_id=request.form["id_torneo"]

        db.session.commit()
        return redirect(url_for('home'))

@app.route('/eliminar-juego/<id_juego>')
def eliminar_juego(id_juego):
    db.session.query(Juego).filter_by(id_juego=int(id_juego)).delete()
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    init_db()
    app.run(debug=True)

