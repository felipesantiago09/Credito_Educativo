from src.controller.estudiante_controller import crear_tablas
from src.gui.credito_gui import MainApp
 
crear_tablas()
print("Tablas verificadas/creadas en PostgreSQL.")
 
MainApp().run()
 