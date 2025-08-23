from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import Enum as _Enum

from db import Base
from enums.tipos import RolEquipo, TipoTorneo


# Crea la tabla de asociacion o tabla de union entre Usuarios y Equipos
class UsuarioEquipo(Base):
    __tablename__ = 'usuarios_equipos'
    __table_args__ = (
        UniqueConstraint('usuario_id', 'equipo_id','torneo_id', name='uq_usuario_equipo_torneo'),
        {'sqlite_autoincrement': True, 'comment': 'Tabla de asociacion entre usuarios y equipos'}
    )
    id_usuario_equipo:Mapped[int] = mapped_column(
        primary_key=True,
        comment='ID de la asociacion entre usuario y equipo'
    )
    usuario_id:Mapped[int] = mapped_column(
        ForeignKey('usuarios.id_usuario')

    )
    equipo_id:Mapped[int] = mapped_column(
        ForeignKey('equipos.id_equipo')
    )
    torneo_id:Mapped[int] = mapped_column(
        ForeignKey('torneos.id_torneo')
    )
    rol_equipo:Mapped[RolEquipo] = mapped_column(
        _Enum(RolEquipo,name='rol_equipo_enum'),
        nullable=False,
        default=RolEquipo.miembro,
        server_default="miembro",
        comment="Rol del jugador en el equipo"
    )