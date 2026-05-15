import sys
sys.path.append('src')

from src.model.connection import Base, engine
from src.model.estudiante_model import Estudiante

Base.metadata.create_all(bind=engine)

print("Tablas creadas")

from src.view.gui.credito_gui import CreditoApp

CreditoApp().run()