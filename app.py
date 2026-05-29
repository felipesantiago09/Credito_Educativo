from flask import Flask
from flask import render_template, request

import sys
sys.path.append( "src" )

from model.estudiante_model import Estudiante
from controller.estudiante_controller import EstudiantesController
from model.logica_Credito import calcular_cuota, calcular_total_abonos, calcular_total_intereses
from model.logica_Credito import ErrorValorCompra, ErrorPlazo, ErrorUsura, ErrorDatos

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
    return render_template("crear_estudiante.html", mensaje="Estudiante insertado exitosamente")

@app.route('/crear_tablas')
def crear_tablas():
    EstudiantesController.crear_tabla()
    return render_template("crear_estudiante.html", mensaje="Tablas creadas exitosamente")

@app.route("/buscar_estudiante")
def buscar_estudiante():
    estudiante_encontrado = EstudiantesController.buscar_estudiante( request.args["id_buscado"] )
    return render_template("estudiante_buscado.html", estudiante=estudiante_encontrado)

@app.route("/calcular_credito")
def calcular_credito():
    error = None
    cuota = None
    total_abonos = None
    total_intereses = None

    monto   = request.args.get("monto")
    tasa    = request.args.get("tasa")
    plazo   = request.args.get("plazo")

    if monto and tasa and plazo:
        try:
            monto_f  = float(monto.replace(',', '.'))
            tasa_f   = float(tasa.replace(',', '.')) / 100
            plazo_i  = int(plazo)

            cuota           = round( calcular_cuota(monto_f, tasa_f, plazo_i), 2 )
            total_abonos    = round( calcular_total_abonos(monto_f, tasa_f, plazo_i), 2 )
            total_intereses = round( calcular_total_intereses(monto_f, tasa_f, plazo_i), 2 )

        except (ErrorValorCompra, ErrorPlazo, ErrorUsura, ErrorDatos) as e:
            error = str(e)
        except ValueError:
            error = "Por favor ingrese solo numeros en todos los campos."

    return render_template("calcular_credito.html",
        monto=monto, tasa=tasa, plazo=plazo,
        cuota=cuota, total_abonos=total_abonos,
        total_intereses=total_intereses, error=error)

if __name__ == '__main__':
    app.run( debug=True )
