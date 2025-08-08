from flask import Blueprint, render_template, request, flash, redirect, url_for

from enums.paginas import PaginaSitio, RefPagina
from enums.tipos import RolEquipo

from services import usuario_equipo_service

usuEquipo_bp=Blueprint('usuEquipos',__name__)

@usuEquipo_bp.route('/usuEquipos')
@usuEquipo_bp.route('/usuEquipos/<indice>')
def usuEquipos(indice=7):
    todos_equipos=usuario_equipo_service.obtener_todos_equipos()
    todos_usuarios=usuario_equipo_service.obtener_todos_usuarios()
    todos_torneos=usuario_equipo_service.obtener_todos_torneos()
    usuarios_equipos=usuario_equipo_service.obtener_todos_usuarios_equipos()
    rol_equipos_enum=RolEquipo
    return render_template('usuarios_equipos.html',
                           indice=indice,
                           paginas_enum=PaginaSitio,
                           referencia_enum=RefPagina,
                           usuarios=todos_usuarios,
                           equipos=todos_equipos,
                           torneos=todos_torneos,
                           usuarios_equipos=usuarios_equipos,
                           roles=rol_equipos_enum
    )

@usuEquipo_bp.route('/afiliar-usuario-equipo', methods=['POST'])
def afiliar_usuario_equipo():
    id_usuario = request.form['contenido_seleccion_jugador']
    id_equipo = request.form['contenido_seleccion_equipo']
    id_torneo = request.form['contenido_seleccion_torneo']
    rol_equipo = request.form['contenido_rol_equipo']

    try:
        usuario_equipo_service.afiliar_usuario_equipo(
            usuario_id=id_usuario,
            equipo_id=id_equipo,
            torneo_id=id_torneo,
            rol_equipo=rol_equipo
        )
        flash('Usuario equipo creado exitosamente!', 'success')
    except ValueError as e:
        flash(f'Error al crear usuario equipo: {str(e)}', 'danger')

    return redirect(url_for('usuEquipos.usuEquipos'))
