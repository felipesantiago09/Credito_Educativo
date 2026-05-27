import psycopg2
from src.model.connection import get_connection
from src.model.estudiante_model import Estudiante


def crear_tablas():
    """Crea la tabla estudiantes en PostgreSQL si no existe."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS estudiantes (
                    id      SERIAL PRIMARY KEY,
                    nombre  VARCHAR(255) NOT NULL,
                    correo  VARCHAR(255) NOT NULL UNIQUE,
                    carrera VARCHAR(255) NOT NULL
                );
            """)
        conn.commit()
    finally:
        conn.close()


def borrar_tablas():
    """Elimina la tabla estudiantes (usar solo en tests o mantenimiento)."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS estudiantes;")
        conn.commit()
    finally:
        conn.close()


def insertar_estudiante(nombre, correo, carrera):
    """
    Inserta un nuevo estudiante y retorna el objeto Estudiante con su id asignado.
    Lanza psycopg2.errors.UniqueViolation si el correo ya existe.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO estudiantes (nombre, correo, carrera)
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (nombre, correo, carrera),
            )
            nuevo_id = cur.fetchone()[0]
        conn.commit()
        return Estudiante(id=nuevo_id, nombre=nombre, correo=correo, carrera=carrera)
    finally:
        conn.close()


def consultar_estudiantes():
    """Retorna una lista de objetos Estudiante con todos los registros."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nombre, correo, carrera FROM estudiantes ORDER BY id;")
            filas = cur.fetchall()
        return [Estudiante(id=f[0], nombre=f[1], correo=f[2], carrera=f[3]) for f in filas]
    finally:
        conn.close()


def buscar_estudiante_por_id(id_estudiante):
    """Retorna un Estudiante por su ID, o None si no existe."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, nombre, correo, carrera FROM estudiantes WHERE id = %s;",
                (id_estudiante,),
            )
            fila = cur.fetchone()
        if fila:
            return Estudiante(id=fila[0], nombre=fila[1], correo=fila[2], carrera=fila[3])
        return None
    finally:
        conn.close()


def buscar_estudiante_por_correo(correo):
    """Retorna un Estudiante por su correo, o None si no existe."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, nombre, correo, carrera FROM estudiantes WHERE correo = %s;",
                (correo,),
            )
            fila = cur.fetchone()
        if fila:
            return Estudiante(id=fila[0], nombre=fila[1], correo=fila[2], carrera=fila[3])
        return None
    finally:
        conn.close()


def actualizar_estudiante(id_estudiante, nombre, correo, carrera):
    """Actualiza todos los campos de un estudiante. Retorna True si se modificó."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE estudiantes
                SET nombre = %s, correo = %s, carrera = %s
                WHERE id = %s;
                """,
                (nombre, correo, carrera, id_estudiante),
            )
            filas_afectadas = cur.rowcount
        conn.commit()
        return filas_afectadas > 0
    finally:
        conn.close()


def eliminar_estudiante(id_estudiante):
    """Elimina un estudiante por ID. Retorna True si se eliminó."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM estudiantes WHERE id = %s;",
                (id_estudiante,),
            )
            filas_afectadas = cur.rowcount
        conn.commit()
        return filas_afectadas > 0
    finally:
        conn.close()
