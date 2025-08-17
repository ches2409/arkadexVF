<tipo>(<área>): <mensaje descriptivo corto y claro>

[Opcional] <cuerpo detallado del commit, explicando el "por qué" y el "qué" si es necesario>


# Ejemplos:
# feat(api): agrega validación para usuarios sin email
# fix(ui): corrige el padding en el componente de login
# refactor(service): simplifica lógica de validación
# test(model): agrega tests para el modelo de predicción


# Tipos Comunes
# feat: Para nuevas funcionalidades o características.
# fix: Para correcciones de errores.
# refactor: Para mejoras en el código sin cambiar la funcionalidad.
# test: Para cambios relacionados con pruebas (unitarias, de integración, etc.).
# docs: Para cambios en la documentación (README, comentarios en el código, etc.).
# style: Para cambios de estilo o formato en el código (sin modificar la lógica).
# chore: Para tareas menores relacionadas con mantenimiento (actualización de dependencias, cambios en el sistema de construcción, etc.).

# Puntos Claves:
# Especificidad y Brevedad: El mensaje debe ser corto pero lo suficientemente descriptivo para que cualquier persona pueda entender el propósito del commit sin necesidad de leer el código.
# Cuerpo Opcional: El cuerpo debe usarse cuando el commit realiza cambios complejos o no obvios, y debe explicar el "por qué" de los cambios. Si el cambio es sencillo, el cuerpo puede omitirse.
# Comentarios de Guía: Mantén los comentarios (como los de ejemplos y tipos) para que sirvan como guía visual. Esto es útil para mantener la consistencia en tu equipo, pero recuerda que debes eliminarlos en los commits reales.

# Recomendaciones Adicionales
# Usar verbos en infinitivo: Utiliza verbos en su forma de infinitivo para describir lo que hace el commit. Ejemplo: agregar, corregir, eliminar, etc.
# Ser breve en el mensaje corto: El mensaje debe ser claro y directo, sin ser excesivamente largo. El objetivo es que cualquiera pueda entender rápidamente el propósito del commit.
# Añadir punto al final del cuerpo: Si se incluye un cuerpo, coloca un punto al final del texto para mayor claridad y consistencia.
# Cuerpo del commit (opcional): El cuerpo es opcional y debe incluirse cuando se realicen cambios complejos o no triviales. Explica el por qué se hicieron los cambios si no es obvio, y el qué exactamente cambió en el código.

# No elimines los comentarios, ayudan como guía visual