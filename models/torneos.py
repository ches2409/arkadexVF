from typing import Optional

from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import Enum as _Enum

from db import Base
from enums.tipos import TipoTorneo, EstadoTorneo


class Torneo(Base):
    __tablename__ = "torneos"
    __table_args__ = {
        'sqlite_autoincrement': True,
        'comment':'Tabla para almacenar los torneos'
    }

    id_torneo:Mapped[int]=mapped_column(Integer, primary_key=True)
    nombre_torneo:Mapped[str]=mapped_column(String(50), nullable=False,unique=True)
    fecha_inicio_torneo:Mapped[DateTime]=mapped_column(
        DateTime,
        nullable=False,
        comment='Fecha de inicio del torneo')
    fecha_final_torneo:Mapped[Optional[DateTime]]=mapped_column(DateTime)
    tipo_torneo:Mapped[TipoTorneo]=mapped_column(
        _Enum(TipoTorneo, name='tipo_torneo_enum'),
        nullable=False,
        default=TipoTorneo.puntos,
        server_default="puntos",
        comment='Tipo de torneo'
    )
    estado_torneo:Mapped[EstadoTorneo]=mapped_column(
        _Enum(EstadoTorneo, name='estado_torneo_enum'),
        nullable=False,
        default=EstadoTorneo.activo,
        server_default="activo",
        comment='Estado del torneo'
    )

    juegos=relationship(
        'Juego',
        back_populates='torneos',
    )

    # def __init__(self,nombre_torneo,fecha_inicio_torneo,fecha_final_torneo,tipo_torneo,estado_torneo):
    #     self.nombre_torneo=nombre_torneo
    #     self.fecha_inicio_torneo=fecha_inicio_torneo
    #     self.fecha_final_torneo=fecha_final_torneo
    #     self.tipo_torneo=tipo_torneo
    #     self.estado_torneo=estado_torneo

    def __repr__(self):
        return f'Torneo: {self.nombre_torneo} ({self.tipo_torneo})'