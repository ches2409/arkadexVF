from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash

import db
from models.torneos import Torneo
from enums.tipos import TipoTorneo, EstadoTorneo
from enums.paginas import PaginaSitio, RefPagina

from services import torneo_service

torneos_bp = Blueprint('torneos', __name__)


@torneos_bp.route('/torneos')
@torneos_bp.route('/torneos/<indice>')
def torneos(indice=4):
    todos_los_torneos = torneo_service.obtener_torneos()
    return render_template('torneos.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           referencia_enum=RefPagina,
                           tipo_torneos_enum=TipoTorneo,
                           estado_torneos_enum=EstadoTorneo,
                           torneos=todos_los_torneos
                           )


@torneos_bp.route('/crear-torneo', methods=['POST'])
def crear_torneo():
    nombre_torneo = request.form["nombre_torneo"]
    fecha_inicio_torneo=datetime.strptime(request.form["fecha_inicio_torneo"], "%Y-%m-%d")
    fecha_final_torneo = request.form["fecha_fin_torneo"]
    fecha_final_torneo = datetime.strptime(fecha_final_torneo, "%Y-%m-%d") if fecha_final_torneo else None
    tipo_torneo=request.form["contenido_tipo_torneo"]
    estado_torneo=request.form["contenido_estado_torneo"]

    try:
        torneo_service.crear_torneo(
            nombre_torneo=nombre_torneo,
            fecha_inicio_torneo=fecha_inicio_torneo,
            fecha_final_torneo=fecha_final_torneo,
            tipo_torneo=tipo_torneo,
            estado_torneo=estado_torneo
        )
        flash(f'El Torneo ({nombre_torneo}) ha sido creado correctamente', 'success')
    except ValueError as e:
        flash(f'Error al crear Torneo: {str(e)}', 'danger')

    return redirect(url_for('torneos.torneos'))

@torneos_bp.route('/editar-torneo/<id_torneo>', methods=['POST'])
def editar_torneo(id_torneo):
    nombre_torneo = request.form["nombre_torneo"]
    fecha_inicio_torneo = datetime.strptime(request.form["fecha_inicio_torneo"], "%Y-%m-%d")
    fecha_final = request.form["fecha_fin_torneo"]
    fecha_final_torneo = datetime.strptime(fecha_final, "%Y-%m-%d") if fecha_final else None
    tipo_torneo = request.form["contenido_tipo_torneo"]
    estado_torneo = request.form["contenido_estado_torneo"]

    try:
        torneo_service.editar_torneo(
            id_torneo=id_torneo,
            nombre_torneo=nombre_torneo,
            fecha_inicio_torneo=fecha_inicio_torneo,
            fecha_final_torneo=fecha_final_torneo,
            tipo_torneo=tipo_torneo,
            estado_torneo=estado_torneo
        )
        flash(f'Se ha actualizado el Torneo ({nombre_torneo}) correctamente', 'success')
    except ValueError as e:
        flash(f'Error al actualizar Torneo: {str(e)}', 'danger')

    return redirect(url_for('torneos.torneos'))


@torneos_bp.route('/eliminar-torneo/<id_torneo>')
def eliminar_torneo(id_torneo):
    db.session.query(Torneo).filter_by(id_torneo=int(id_torneo)).delete()
    db.session.commit()
    return redirect(url_for('torneos.torneos'))

