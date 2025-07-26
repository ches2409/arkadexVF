from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base

class Juego(Base):
    __tablename__ = 'juegos'
    __table_args__ = {
        'sqlite_autoincrement' : True,
        'comment': 'Tabla para los distintos juegos',
    }
    id_juego:Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre_juego:Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    descripcion_juego:Mapped[str] = mapped_column(String(150))

    # FK hacia Torneos (torneos.id_torneo)
    torneo_id:Mapped[int]=mapped_column(
        ForeignKey('torneos.id_torneo', ondelete='RESTRICT'),
        nullable=False,
    )

    # Relacion con el objeto torneo
    torneos:Mapped["Torneo"]=relationship(
        "Torneo",
        back_populates="juegos",
    )

    def __repr__(self):
        return f'Juego creado con exrito: {self.nombre_juego}'

