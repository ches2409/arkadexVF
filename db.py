from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Conexion con SQLite
engine=create_engine('sqlite:///database/torneos.db',echo=True)

# Crear sesion para interactuar con la BD
Session=sessionmaker(bind=engine)
session=Session()

class Base(DeclarativeBase):
    pass

def init_db():
    Base.metadata.create_all(bind=engine)
    # Base.metadata.drop_all(bind=engine, checkfirst=True)