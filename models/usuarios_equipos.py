from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import Enum as _Enum

from db import Base
from enums.tipos import RolEquipo, TipoTorneo


# Crea la tabla de asociacion o tabla de union entre Usuarios y Equipos
class UsuarioEquipo(Base):
    __tablename__ = 'usuarios_equipos'
    # __table_args__ = {
    #     'sqlite_autoincrement': True,
    #     'comment':'Tabla de usuariose con su respectivo equipo'
    # }

    usuario_id:Mapped[int] = mapped_column(
        ForeignKey('usuarios.id_usuario'),
        primary_key=True
    )
    equipo_id:Mapped[int] = mapped_column(
        ForeignKey('equipos.id_equipo'),
        primary_key=True
    )
    torneo_id:Mapped[int] = mapped_column(
        ForeignKey('torneos.id_torneo'),
        primary_key=True
    )
    rol_equipo:Mapped[RolEquipo] = mapped_column(
        _Enum(RolEquipo,name='rol_equipo_enum'),
        nullable=False,
        default=RolEquipo.miembro,
        server_default="miembro",
        comment="Rol del jugador en el equipo"
    )