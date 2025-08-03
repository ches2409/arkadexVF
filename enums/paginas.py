import enum

class PaginaSitio(enum.Enum):
    inicio="inicio"
    roles="roles"
    usuarios="usuarios"
    torneos="torneos"
    juegos="juegos"
    equipos="equipos"

class RefPagina(enum.Enum):
    inicio="inicio.inicio"
    roles="roles.roles"
    usuarios="usuarios.usuarios"
    torneos="torneos.torneos"
    juegos="juegos.juegos"