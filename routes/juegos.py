from flask import Blueprint, render_template, request, redirect, url_for, flash

import db
from models.juegos import Juego
from models.torneos import Torneo
from enums.paginas import PaginaSitio, RefPagina

from services import juego_service

juegos_bp = Blueprint('juegos', __name__)


@juegos_bp.route('/juegos')
@juegos_bp.route('/juegos/<indice>')
def juegos(indice=5):
    # indice=4
    todos_los_torneos = juego_service.obtener_todos_torneos()
    juegos_con_torneos = juego_service.obtener_juegos_con_torneos()
    return render_template('juegos.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           referencia_enum=RefPagina,
                           torneos=todos_los_torneos,
                           juegos=juegos_con_torneos
                           )


@juegos_bp.route('/crear-juego', methods=['POST'])
def crear_juego():
    nombre_juego = request.form["nombre_Juego"]
    descripcion_juego = request.form["descripcion_juego"]
    rol_torneo=request.form["id_torneo"]

    try:
        juego_service.crear_juego(
            nombre_juego=nombre_juego,
            descripcion_juego=descripcion_juego,
            torneo_id=rol_torneo
        )
        flash(f'El juego {{ nombre_juego }} creado correctamente', 'success')

    except ValueError as e:
        flash(f'Error al crear Juego: {str(e)}', 'danger')

    return redirect(url_for('juegos.juegos'))

@juegos_bp.route('/editar-juego/<id_juego>', methods=['POST'])
def editar_juego(id_juego):
    nombre_juego = request.form["nombre_juego"]
    descripcion_juego = request.form["descripcion_juego"]
    torneo_id = request.form["id_torneo"]

    try:
        juego_service.editar_juego(
            id_juego=id_juego,
            nombre_juego=nombre_juego,
            descripcion_juego=descripcion_juego,
            torneo_id=torneo_id
        )
        flash(f"Se actualizo el juego correctamente", "success")
    except ValueError as e:
        flash(f'Error al editar Juego: {str(e)}', 'danger')

    return redirect(url_for('juegos.juegos'))

    # juego=db.session.query(Juego).get(id_juego)
    # if juego is None:
    #     return redirect(url_for('juegos.juegos'))
    # else:
    #     juego.nombre_juego=request.form["nombre_juego"]
    #     juego.descripcion_juego=request.form["descripcion_juego"]
    #     juego.torneo_id=request.form["id_torneo"]
    #
    #     db.session.commit()
    #     return redirect(url_for('juegos.juegos'))

@juegos_bp.route('/eliminar-juego/<id_juego>')
def eliminar_juego(id_juego):

    try:
        juego_service.elimnar_juego(id_juego)
        flash(f'Juego eliminado correctamente', 'info')
    except ValueError as e:
        db.session.rollback()
        flash(f'Error al eliminar el Juego:{str(e)}','danger')

    return redirect(url_for('juegos.juegos'))

