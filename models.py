from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Rol(Base):

    # Mapear
    __tablename__ = 'roles'
    __table_args__ = {
        'sqlite_autoincrement': True,
        'comment': 'Tabla que almacena los Roles de los participantes',
    }
    id_rol:Mapped[int]=mapped_column(Integer, primary_key=True)
    nombre_rol:String=mapped_column(String(50), nullable=False)
    descripcion_rol:String=mapped_column(String(100), nullable=False)

    def __init__(self,nombre_rol,descripcion_rol):
        self.nombre_rol = nombre_rol
        self.descripcion_rol = descripcion_rol

    def __repr__(self):
        return f'{self.nombre_rol} {self.descripcion_rol}'