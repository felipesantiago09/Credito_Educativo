from sqlalchemy import Column, Integer, String
from src.model.connection import Base

class Estudiante(Base):

    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True)
    carrera = Column(String)