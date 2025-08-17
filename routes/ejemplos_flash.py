from flask import Blueprint, render_template, flash, redirect, url_for
from enums.paginas import PaginaSitio, RefPagina

ejemplos_flash_bp = Blueprint('ejemplos_flash', __name__)

@ejemplos_flash_bp.route('/ejemplos-flash')
def ejemplos_flash():
    return render_template('ejemplos_flash.html',
                          indice=0,
                          paginas_enum=PaginaSitio,
                          referencia_enum=RefPagina)

@ejemplos_flash_bp.route('/mostrar-mensaje-success')
def mostrar_mensaje_success():
    flash('Este es un mensaje de éxito', 'success')
    return redirect(url_for('ejemplos_flash.ejemplos_flash'))

@ejemplos_flash_bp.route('/mostrar-mensaje-info')
def mostrar_mensaje_info():
    flash('Este es un mensaje informativo', 'info')
    return redirect(url_for('ejemplos_flash.ejemplos_flash'))

@ejemplos_flash_bp.route('/mostrar-mensaje-warning')
def mostrar_mensaje_warning():
    flash('Este es un mensaje de advertencia', 'warning')
    return redirect(url_for('ejemplos_flash.ejemplos_flash'))

@ejemplos_flash_bp.route('/mostrar-mensaje-danger')
def mostrar_mensaje_danger():
    flash('Este es un mensaje de error', 'danger')
    return redirect(url_for('ejemplos_flash.ejemplos_flash'))

@ejemplos_flash_bp.route('/mostrar-mensaje-primary')
def mostrar_mensaje_primary():
    flash('Este es un mensaje primario', 'primary')
    return redirect(url_for('ejemplos_flash.ejemplos_flash'))

@ejemplos_flash_bp.route('/mostrar-mensaje-secondary')
def mostrar_mensaje_secondary():
    flash('Este es un mensaje secundario', 'secondary')
    return redirect(url_for('ejemplos_flash.ejemplos_flash'))

@ejemplos_flash_bp.route('/mostrar-mensaje-light')
def mostrar_mensaje_light():
    flash('Este es un mensaje claro', 'light')
    return redirect(url_for('ejemplos_flash.ejemplos_flash'))

@ejemplos_flash_bp.route('/mostrar-mensaje-dark')
def mostrar_mensaje_dark():
    flash('Este es un mensaje oscuro', 'dark')
    return redirect(url_for('ejemplos_flash.ejemplos_flash'))

@ejemplos_flash_bp.route('/mostrar-multiples-mensajes')
def mostrar_multiples_mensajes():
    flash('Primer mensaje de éxito', 'success')
    flash('Segundo mensaje informativo', 'info')
    flash('Tercer mensaje de advertencia', 'warning')
    return redirect(url_for('ejemplos_flash.ejemplos_flash'))