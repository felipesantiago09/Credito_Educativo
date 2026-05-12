import sys
sys.path.append('src')

from src.model.connection import engine
from src.model.base import Base

from src.model.estudiante_model import Estudiante

Base.metadata.create_all(engine)

from src.view.gui.credito_gui import CreditoApp

CreditoApp().run()