# Sistema de Mensajes Flash en Arkadex2

Este documento explica cómo se ha implementado el sistema de mensajes flash en el proyecto Arkadex2 utilizando la funcionalidad incorporada de Flask.

## ¿Qué son los mensajes flash?

Los mensajes flash son una forma de enviar información de una solicitud a la siguiente. Son especialmente útiles para mostrar mensajes de éxito, error, advertencia o información al usuario después de realizar una acción, como enviar un formulario o iniciar sesión.

## Configuración básica

### 1. Clave secreta

Para utilizar mensajes flash, es necesario configurar una clave secreta en la aplicación Flask. Esto se hace en el archivo `main.py`:

```python
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
```

### 2. Plantilla base

Los mensajes flash se muestran en la plantilla base `layout.html` para que estén disponibles en todas las páginas:

```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

## Uso de mensajes flash

### Importar la función flash

```python
from flask import flash
```

### Crear un mensaje flash

```python
flash('Mensaje de éxito', 'success')
```

El primer parámetro es el mensaje a mostrar, y el segundo es la categoría. Las categorías disponibles son:

- `success`: Para mensajes de éxito (verde)
- `info`: Para mensajes informativos (azul claro)
- `warning`: Para advertencias (amarillo)
- `danger`: Para errores (rojo)
- `primary`: Azul principal de Bootstrap
- `secondary`: Gris secundario de Bootstrap
- `light`: Fondo claro
- `dark`: Fondo oscuro

## Ejemplos implementados

### 1. Mensajes en CRUD de usuarios

Se han implementado mensajes flash en las operaciones CRUD de usuarios:

- Crear usuario: Muestra un mensaje de éxito o error
- Editar usuario: Muestra un mensaje de éxito, advertencia o error
- Eliminar usuario: Muestra un mensaje informativo, advertencia o error

### 2. Autenticación

Se ha creado un ejemplo de sistema de autenticación con mensajes flash:

- Login exitoso: Muestra un mensaje de bienvenida
- Login fallido: Muestra un mensaje de error
- Logout: Muestra un mensaje informativo

### 3. Página de ejemplos

Se ha creado una página de ejemplos en `/ejemplos-flash` que muestra todos los tipos de mensajes flash disponibles.

## Filtrado de mensajes por categoría

También es posible filtrar los mensajes por categoría en las plantillas:

```html
{% with errors = get_flashed_messages(category_filter=["error", "danger"]) %}
    {% if errors %}
        {% for error in errors %}
            <div class="alert alert-danger">{{ error }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

Esto mostraría solo los mensajes de las categorías "error" y "danger".

## Consideraciones

- Los mensajes flash solo se muestran una vez y luego se eliminan automáticamente
- Se almacenan en la sesión del usuario, por lo que requieren una clave secreta
- Si los mensajes son muy grandes, pueden causar problemas con el tamaño de la cookie de sesión