from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Usuario(Base):

    __tablename__ = 'usuarios'
    __table_args__ = {
        'sqlite_autoincrement': True,
        'comment':'Tabla de usuarios'
    }

    id_usuario:Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre_usuario:Mapped[str] = mapped_column(String(50), nullable=False)
    email_usuario:Mapped[str] = mapped_column(String(100), nullable=False)
    password_usuario:Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_registro:Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment='Fecha de registro')

    # FK hacia rol (roles.id_rol)
    rol_id:Mapped[int] = mapped_column(
        ForeignKey('roles.id_rol', ondelete='RESTRICT'),
        nullable=False,
    )

    # Relacion con objeto rol
    roles:Mapped["Rol"]=relationship(
        "Rol",
        back_populates="usuarios",
    )


    def __init__(self,nombre_usuario,email_usuario,password_usuario,fecha_registro,rol_id):
        self.nombre_usuario = nombre_usuario
        self.email_usuario = email_usuario
        self.password_usuario = password_usuario
        self.fecha_registro = fecha_registro
        self.rol_id = rol_id

    def __repr__(self):
        return f'Se ha creado {self.nombre_usuario} - {self.email_usuario}'