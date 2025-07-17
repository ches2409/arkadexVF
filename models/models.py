# from sqlalchemy import Integer, String, DateTime, func, ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column, relationship
#
# from db import Base
#
#
# class Rol(Base):
#
#     # Mapear
#     __tablename__ = 'roles'
#     __table_args__ = {
#         'sqlite_autoincrement': True,
#         'comment': 'Tabla que almacena los Roles de los participantes',
#     }
#     id_rol:Mapped[int]=mapped_column(Integer, primary_key=True)
#     nombre_rol:Mapped[str]=mapped_column(String(50), nullable=False)
#     descripcion_rol:Mapped[str]=mapped_column(String(100), nullable=False)
#
#     # Relacion inversa con usuarios
#     rol:Mapped[list["Rol"]]=relationship(
#         "Rol",
#         back_populates="usuarios",
#
#     )
#
#
#     def __init__(self,nombre_rol,descripcion_rol):
#         self.nombre_rol = nombre_rol
#         self.descripcion_rol = descripcion_rol
#
#     def __repr__(self):
#         return f'{self.nombre_rol} {self.descripcion_rol}'
#
# class Usuario(Base):
#
#     __tablename__ = 'usuarios'
#     __mapper_args__ = {
#         'sqlite_autoincrement': True,
#         'comment':'Tabla de usuarios'
#     }
#     id_usuario:Mapped[int] = mapped_column(Integer, primary_key=True)
#     nombre_usuario:Mapped[str] = mapped_column(String(50), nullable=False)
#     email_usuario:Mapped[str] = mapped_column(String(100), nullable=False)
#     password_usuario:Mapped[str] = mapped_column(String(50), nullable=False)
#     fecha_registro:Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now(),comment='Fecha de registro')
#
#     # FK hacia rol
#     id_rol:Mapped[int] = mapped_column(ForeignKey('usuarios.id_rol'))
#
#     # Relacion con objeto rol
#     rol:Mapped[Rol]=relationship(
#         "Rol",
#         back_populates="usuarios",
#     )