from flask import Blueprint, render_template, request, redirect, url_for

import db
from enums.paginas import PaginaSitio
from enums.tipos import EstadoEquipo
from models.equipos import Equipo

equipos_bp=Blueprint('equipos', __name__)


@equipos_bp.route('/equipos')
@equipos_bp.route('/equipos/<indice>')
def equipos(indice=6):

    todos_los_equipos=db.session.query(Equipo).all()

    return render_template('equipos.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           estado_enum=EstadoEquipo,
                           equipos=todos_los_equipos,
                           )


# Crear un nuevo equipo
@equipos_bp.route('/crear-equipo', methods=['GET', 'POST'])
def crear_equipo():
    nombre_equipo=request.form['nombre_equipo']
    descripcion_equipo=request.form['descripcion_equipo']
    estado_equipo=request.form['estado_equipo']

    equipo=Equipo(nombre_equipo=nombre_equipo, descripcion_equipo=descripcion_equipo, estado_equipo=estado_equipo)
    db.session.add(equipo)
    db.session.commit()
    return redirect(url_for('equipos.equipos'))

# Editar un equipo
@equipos_bp.route('/editar-equipo/<id_equipo>', methods=['GET', 'POST'])
def editar_equipo(id_equipo):
    equipo=db.session.query(Equipo).get(id_equipo)
    if equipo is None:
        return redirect(url_for('equipos.equipos'))
    else:
        equipo.nombre_equipo=request.form['nombre_equipo']
        equipo.descripcion_equipo=request.form['descripcion_equipo']
        equipo.estado_equipo=request.form['estado_equipo']
    db.session.commit()
    return redirect(url_for('equipos.equipos'))

# Eliminar un equipo
@equipos_bp.route('/eliminar-equipo/<id_equipo>', methods=['GET', 'POST'])
def eliminar_equipo(id_equipo):
    db.session.query(Equipo).filter_by(id_equipo=id_equipo).delete()
    db.session.commit()
    return redirect(url_for('equipos.equipos'))