from flask import Blueprint, render_template

from enums.paginas import PaginaSitio, RefPagina
from enums.tipos import RolEquipo

from services import usuario_equipo_service

usuEquipo_bp=Blueprint('usuarios_equipos',__name__)

@usuEquipo_bp.route('/usuarios_equipos')
@usuEquipo_bp.route('/usuarios_equipos/<indice>')
def usuarios_equipos(indice=7):
    todos_equipos=usuario_equipo_service.obtener_todos_equipos()
    todos_usuarios=usuario_equipo_service.obtener_todos_usuarios()
    todos_torneos=usuario_equipo_service.obtener_todos_torneos()
    rol_equipos_enum=RolEquipo
    return render_template('usuarios_equipos.html',

                           indice=indice,
                           paginas_enum=PaginaSitio,
                           referencia_enum=RefPagina,
                           usuarios=todos_usuarios,
                           equipos=todos_equipos,
                           torneos=todos_torneos,
                           roles=rol_equipos_enum
    )
