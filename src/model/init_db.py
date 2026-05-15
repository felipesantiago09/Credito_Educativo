print("INICIANDO...")

from src.model.connection import engine, Base
from src.model.estudiante_model import Estudiante

print("MODELO CARGADO")

Base.metadata.create_all(engine)

print("Tablas creadas correctamente")