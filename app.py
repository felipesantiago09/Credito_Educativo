from flask import Flask
from flask import render_template, request

import sys
sys.path.append( "src" )

from model.estudiante_model import Estudiante
from controller.estudiante_controller import EstudiantesController

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("crear_estudiante.html")

@app.route('/guardar_estudiante')
def guardar_estudiante():

    estudiante = Estudiante( id=None, nombre="", correo="", carrera="" )
    estudiante.nombre  = request.args["nombre"]
    estudiante.correo  = request.args["correo"]
    estudiante.carrera = request.args["carrera"]

    EstudiantesController.insertar( estudiante )

    return "Estudiante insertado exitosamente"

@app.route('/crear_tablas')
def crear_tablas():
    EstudiantesController.crear_tabla()
    return "Tablas creadas exitosamente"

@app.route("/buscar_estudiante")
def buscar_estudiante():
    estudiante_encontrado = EstudiantesController.buscar_estudiante( request.args["id_buscado"] )
    return render_template("estudiante_buscado.html", estudiante=estudiante_encontrado)

if __name__ == '__main__':
    app.run( debug=True )
