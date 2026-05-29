import sys
sys.path.append( "." )
sys.path.append( "src" )

from model.connection import get_connection
from model.estudiante_model import Estudiante


class EstudiantesController:

    def crear_tabla():
        conn = get_connection()
        with open( "sql/CrearTabla.sql", "r" ) as archivo:
            consulta = archivo.read()
        with conn.cursor() as cur:
            cur.execute( consulta )
        conn.commit()
        conn.close()

    def borrar_tabla():
        conn = get_connection()
        with open( "sql/eliminarBorrar.sql", "r" ) as archivo:
            consulta = archivo.read()
        with conn.cursor() as cur:
            cur.execute( consulta )
        conn.commit()
        conn.close()

    def insertar( estudiante : Estudiante ):
        """ Recibe una instancia de Estudiante y la inserta en la tabla """
        conn = get_connection()
        with open( "sql/insertar.sql", "r" ) as archivo:
            consulta = archivo.read()
        consulta = consulta.format(
            nombre  = estudiante.nombre,
            correo  = estudiante.correo,
            carrera = estudiante.carrera
        )
        with conn.cursor() as cur:
            cur.execute( consulta )
        conn.commit()
        conn.close()

    def buscar_estudiante( id_estudiante ) -> Estudiante:
        """ Trae un estudiante dado su id """
        conn = get_connection()
        with open( "sql/buscar.sql", "r" ) as archivo:
            consulta = archivo.read()
        consulta = consulta.format( id=id_estudiante )
        with conn.cursor() as cur:
            cur.execute( consulta )
            fila = cur.fetchone()
        conn.close()
        if fila is None:
            return None
        return Estudiante( id=fila[0], nombre=fila[1], correo=fila[2], carrera=fila[3] )

    def consultar_todos() -> list:
        """ Trae todos los estudiantes de la tabla """
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute( "select id, nombre, correo, carrera from estudiantes order by id" )
            lista = cur.fetchall()
        conn.close()
        return [ Estudiante( id=f[0], nombre=f[1], correo=f[2], carrera=f[3] ) for f in lista ]

    def actualizar( id_estudiante, nombre,):
        conn = get_connection()
        with open( "sql/actualizar.sql", "r" ) as archivo:
            consulta = archivo.read()
        consulta = consulta.format(
            nombre  = nombre,
            id      = id_estudiante
        )
        with conn.cursor() as cur:
            cur.execute( consulta )
        conn.commit()
        conn.close()

    def eliminar( id_estudiante ):
        """ Elimina un estudiante por su id """
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute( f"delete from estudiantes where id = {id_estudiante}" )
        conn.commit()
        conn.close()


# ── Funciones sueltas para compatibilidad con main.py ──────────────────────────

def crear_tablas():
    EstudiantesController.crear_tabla()

def borrar_tablas():
    EstudiantesController.borrar_tabla()

def insertar_estudiante(nombre, correo, carrera):
    e = Estudiante(id=None, nombre=nombre, correo=correo, carrera=carrera)
    EstudiantesController.insertar( e )

def consultar_estudiantes():
    return EstudiantesController.consultar_todos()

def buscar_estudiante_por_id(id_estudiante):
    return EstudiantesController.buscar_estudiante( id_estudiante )

def actualizar_estudiante( id_estudiante, nombre ):
    EstudiantesController.actualizar( id_estudiante, nombre )
    
def eliminar_estudiante(id_estudiante):
    EstudiantesController.eliminar( id_estudiante )
