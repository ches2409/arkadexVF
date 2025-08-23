import enum

class PaginaSitio(enum.Enum):
    inicio="inicio"
    roles="roles"
    usuarios="jugadores"
    torneos="torneos"
    juegos="juegos"
    equipos="facciones"
    usuarios_equipos="Afiliacion"

class RefPagina(enum.Enum):
    inicio="inicio.inicio"
    roles="roles.roles"
    usuarios="usuarios.usuarios"
    torneos="torneos.torneos"
    juegos="juegos.juegos"
    equipos="equipos.equipos"
    usuarios_equipos="usuarios_equipos.usuarios_equipos"