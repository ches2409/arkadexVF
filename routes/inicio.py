from flask import Blueprint, render_template
from enums.paginas import PaginaSitio, RefPagina

# Crear el blueprint
inicio_bp = Blueprint('inicio', __name__)

@inicio_bp.route('/')
@inicio_bp.route('/<indice>')
def inicio(indice=1):
    return render_template('inicio.html',
                           indice=indice,
                           referencia_enum=RefPagina,
                           paginas_enum=PaginaSitio
                           )