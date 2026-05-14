import sys
sys.path.append('src')

from src.model.connection import Base, engine
from src.model.estudiante_model import Estudiante

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Tablas creadas")

from src.controller.estudiante_controller import *

# INSERT
insertar_estudiante(
    "Esteban",
    "esteban@gmail.com",
    "Ingenieria"
)

# SELECT
consultar_estudiantes()

# UPDATE
actualizar_estudiante(1, "Felipe")

# SELECT
consultar_estudiantes()

# DELETE
eliminar_estudiante(1)

# SELECT
consultar_estudiantes()


from src.view.gui.credito_gui import CreditoApp

CreditoApp().run()