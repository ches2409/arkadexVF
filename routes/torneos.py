from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for

import db
from models.torneos import Torneo
from enums.tipos import TipoTorneo, EstadoTorneo
from enums.paginas import PaginaSitio, RefPagina

torneos_bp = Blueprint('torneos', __name__)


@torneos_bp.route('/torneos')
@torneos_bp.route('/torneos/<indice>')
def torneos(indice=4):
    todos_los_torneos = db.session.query(Torneo).all()
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

    torneo=Torneo(nombre_torneo=nombre_torneo,fecha_inicio_torneo=fecha_inicio_torneo,fecha_final_torneo=fecha_final_torneo,tipo_torneo=tipo_torneo,estado_torneo=estado_torneo)

    db.session.add(torneo)
    db.session.commit()
    return redirect(url_for('torneos.torneos'))

@torneos_bp.route('/editar-torneo/<id_torneo>', methods=['POST'])
def editar_torneo(id_torneo):
    torneo=db.session.query(Torneo).get(id_torneo)
    if torneo is None:
        return redirect(url_for('torneos.torneos'))
    else:
        torneo.nombre_torneo=request.form["nombre_torneo"]
        torneo.fecha_inicio_torneo=datetime.strptime(request.form["fecha_inicio_torneo"],"%Y-%m-%d")
        fecha_final=request.form["fecha_fin_torneo"]
        torneo.fecha_final_torneo = datetime.strptime(fecha_final, "%Y-%m-%d") if fecha_final else None
        torneo.tipo_torneo=request.form["contenido_tipo_torneo"]
        torneo.estado_torneo=request.form["contenido_estado_torneo"]
        db.session.commit()
        return redirect(url_for('torneos.torneos'))

@torneos_bp.route('/eliminar-torneo/<id_torneo>')
def eliminar_torneo(id_torneo):
    db.session.query(Torneo).filter_by(id_torneo=int(id_torneo)).delete()
    db.session.commit()
    return redirect(url_for('torneos.torneos'))

