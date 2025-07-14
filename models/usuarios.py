from db import Base


class Usuario(Base):

    def __init__(self,nombre_usuario,email_usuario,password_usuario,fecha_registro,rol):
        self.nombre_usuario = nombre_usuario
        self.email_usuario = email_usuario
        self.password_usuario = password_usuario
        self.fecha_registro = fecha_registro
        self.rol = rol

    def __repr__(self):
        return f'Se ha creado {self.nombre_usuario} - {self.email_usuario}'