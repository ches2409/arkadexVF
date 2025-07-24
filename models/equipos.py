from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from db import Base

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
    estado_equipo:Mapped[str]=mapped_column(String(50), nullable=False)

    def __repr__(self):
        return f"Se ha creado el equipo {self.nombre_equipo}"