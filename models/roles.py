from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import Enum as _Enum

from db import Base
from enums.tipos import RolUsuario


class Rol(Base):
    '''
    Crea una clase llamada Rol
    Esta clase permite crear una clase de rol
    '''

    # Mapear
    __tablename__ = 'roles'
    __table_args__ = {
        'sqlite_autoincrement': True,
        'comment': 'Tabla que almacena los Roles de los participantes',
    }

    id_rol:Mapped[int]=mapped_column(Integer, primary_key=True)
    nombre_rol:Mapped[RolUsuario]=mapped_column(
        _Enum(RolUsuario,name='rol_usuario_enum'),
        nullable=False,
        default=RolUsuario.participante,
        server_default="participante",
        comment='Nombre del rol de usuario'
    )
    descripcion_rol:Mapped[str]=mapped_column(String(100))

    # Relacion inversa con usuarios
    usuarios:Mapped[list["Usuario"]]=relationship(
        "Usuario",
        back_populates="roles",

    )

    # def __init__(self,nombre_rol,descripcion_rol):
    #     self.nombre_rol = nombre_rol
    #     self.descripcion_rol = descripcion_rol

    def __repr__(self):
        return f'{self.nombre_rol} {self.descripcion_rol}'