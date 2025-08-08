from flask import Blueprint, render_template, request, redirect, url_for, flash

import db
from enums.paginas import PaginaSitio, RefPagina
from enums.tipos import EstadoEquipo
from models.equipos import Equipo
from services import equipo_service

equipos_bp=Blueprint('equipos', __name__)


@equipos_bp.route('/equipos')
@equipos_bp.route('/equipos/<indice>')
def equipos(indice=6):

    todos_los_equipos=equipo_service.obtener_todos_equipos()

    return render_template('equipos.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           referencia_enum=RefPagina,
                           estado_enum=EstadoEquipo,
                           equipos=todos_los_equipos,
                           )

# Crear un nuevo equipo
@equipos_bp.route('/crear-equipo', methods=['GET', 'POST'])
def crear_equipo():
    nombre_equipo=request.form['nombre_equipo']
    descripcion_equipo=request.form['descripcion_equipo']
    estado_equipo=request.form['estado_equipo']

    try:
        equipo_service.crear_equipo(
            nombre_equipo=nombre_equipo,
            descripcion_equipo=descripcion_equipo,
            estado_equipo=estado_equipo
        )
        flash('El equipo creado exitosamente!','success')
    except ValueError as e:
        flash(f'Error:  {str(e)}','danger')

    return redirect(url_for('equipos.equipos'))

# Editar un equipo
@equipos_bp.route('/editar-equipo/<id_equipo>', methods=['GET', 'POST'])
def editar_equipo(id_equipo):
    nombre_equipo = request.form['nombre_equipo']
    descripcion_equipo = request.form['descripcion_equipo']
    estado_equipo = request.form['estado_equipo']

    try:
        equipo_service.editar_equipo(
            id_equipo=id_equipo,
            nombre_equipo=nombre_equipo,
            descripcion_equipo=descripcion_equipo,
            estado_equipo=estado_equipo
        )
        flash('El equipo ha sido actualizado exitosamente!', 'success')
    except ValueError as e:
        flash(f'Error: {str(e)}','danger')

    return redirect(url_for('equipos.equipos'))

# Eliminar un equipo
@equipos_bp.route('/eliminar-equipo/<id_equipo>', methods=['GET', 'POST'])
def eliminar_equipo(id_equipo):

    try:
        equipo_service.eliminar_equipo(id_equipo)
        flash('El equipo se ha eliminado exitosamente!', 'info')
    except ValueError as e:
        db.session.rollback()
        flash(f'Error al eliminar el equipo:  {str(e)}','danger')

    return redirect(url_for('equipos.equipos'))