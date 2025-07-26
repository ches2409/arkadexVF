from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import Enum as _Enum

from db import Base
from enums.tipos import EstadoEquipo, EstadoTorneo


class Equipo(Base):

    __tablename__ = "equipos"
    __table_args__ = {
        'sqlite_autoincrement': True,
        'comment': 'Tabla para almacenar los equipos participantes',
    }

    id_equipo:Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre_equipo:Mapped[str]=mapped_column(String(50), nullable=False)
    descripcion_equipo:Mapped[str]=mapped_column(String(150))
    fecha_creacion:Mapped[DateTime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment='Fecha de creacion del equipo',
    )
    estado_equipo:Mapped[EstadoEquipo]=mapped_column(
        _Enum(EstadoEquipo,name="estado_equipo_enum"),
        nullable=False,
        default=EstadoTorneo.activo,
        server_default="activo",
        comment='Estado en el que se encuentra el equipo',
    )

    def __repr__(self):
        return f"Se ha creado el equipo {self.nombre_equipo}"