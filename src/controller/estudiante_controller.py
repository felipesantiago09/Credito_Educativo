from src.model.connection import Session
from src.model.estudiante_model import Estudiante

def insertar_estudiante(nombre, correo, carrera):

    db = Session()

    nuevo = Estudiante(
        nombre=nombre,
        correo=correo,
        carrera=carrera
    )

    db.add(nuevo)

    db.commit()

    db.close()

    print("Insertado")

def consultar_estudiantes():

    db = Session()

    estudiantes = db.query(Estudiante).all()

    db.close()

    return estudiantes

def actualizar_estudiante(id_estudiante, nuevo_nombre):

    db = Session()

    estudiante = db.query(Estudiante).filter(
        Estudiante.id == id_estudiante
    ).first()

    if estudiante:

        estudiante.nombre = nuevo_nombre

        db.commit()

        print("Actualizado")

    db.close()

def eliminar_estudiante(id_estudiante):

    db = Session()

    estudiante = db.query(Estudiante).filter(
        Estudiante.id == id_estudiante
    ).first()

    if estudiante:

        db.delete(estudiante)

        db.commit()

        print("Eliminado")

    db.close()