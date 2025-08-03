from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload

import db
from models.juegos import Juego
from models.torneos import Torneo
from enums.paginas import PaginaSitio, RefPagina

juegos_bp = Blueprint('juegos', __name__)


@juegos_bp.route('/juegos')
@juegos_bp.route('/juegos/<indice>')
def juegos(indice=5):
    # indice=4
    todos_los_torneos = db.session.query(Torneo).all()
    juegos_con_torneos = db.session.query(Juego).options(joinedload(Juego.torneos)).all()
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

    juego=Juego(nombre_juego=nombre_juego,descripcion_juego=descripcion_juego,torneo_id=rol_torneo)
    db.session.add(juego)
    db.session.commit()
    return redirect(url_for('juegos.juegos'))

@juegos_bp.route('/editar-juego/<id_juego>', methods=['POST'])
def editar_juego(id_juego):
    juego=db.session.query(Juego).get(id_juego)
    if juego is None:
        return redirect(url_for('juegos.juegos'))
    else:
        juego.nombre_juego=request.form["nombre_juego"]
        juego.descripcion_juego=request.form["descripcion_juego"]
        juego.torneo_id=request.form["id_torneo"]

        db.session.commit()
        return redirect(url_for('juegos.juegos'))

@juegos_bp.route('/eliminar-juego/<id_juego>')
def eliminar_juego(id_juego):
    db.session.query(Juego).filter_by(id_juego=int(id_juego)).delete()
    db.session.commit()
    return redirect(url_for('juegos.juegos'))
