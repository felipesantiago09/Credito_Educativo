import pytest
import psycopg2
from src.model.estudiante_model import Estudiante


# ── helpers para operar sobre la conexión de test directamente ──────────────

def _insertar(conn, nombre, correo, carrera):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO estudiantes (nombre, correo, carrera) VALUES (%s, %s, %s) RETURNING id;",
            (nombre, correo, carrera),
        )
        nuevo_id = cur.fetchone()[0]
    conn.commit()
    return Estudiante(id=nuevo_id, nombre=nombre, correo=correo, carrera=carrera)


def _buscar_por_correo(conn, correo):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, nombre, correo, carrera FROM estudiantes WHERE correo = %s;",
            (correo,),
        )
        fila = cur.fetchone()
    return Estudiante(id=fila[0], nombre=fila[1], correo=fila[2], carrera=fila[3]) if fila else None


def _buscar_por_nombre(conn, nombre):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, nombre, correo, carrera FROM estudiantes WHERE nombre = %s;",
            (nombre,),
        )
        fila = cur.fetchone()
    return Estudiante(id=fila[0], nombre=fila[1], correo=fila[2], carrera=fila[3]) if fila else None


def _listar(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, nombre, correo, carrera FROM estudiantes ORDER BY id;")
        filas = cur.fetchall()
    return [Estudiante(id=f[0], nombre=f[1], correo=f[2], carrera=f[3]) for f in filas]


# ── INSERTAR ─────────────────────────────────────────────────────────────────

def test_insertar_estudiante(conn_test):
    """Un estudiante insertado debe poder recuperarse con sus datos correctos."""
    _insertar(conn_test, "Juan", "juan@test.com", "Ingenieria")

    resultado = _buscar_por_correo(conn_test, "juan@test.com")

    assert resultado is not None
    assert resultado.nombre == "Juan"
    assert resultado.carrera == "Ingenieria"


def test_insertar_varios_estudiantes(conn_test):
    """Al insertar varios estudiantes, todos deben aparecer en la lista."""
    _insertar(conn_test, "Ana", "ana@test.com", "Medicina")
    _insertar(conn_test, "Luis", "luis@test.com", "Derecho")

    lista = _listar(conn_test)

    assert len(lista) == 2
    nombres = [e.nombre for e in lista]
    assert "Ana" in nombres
    assert "Luis" in nombres


def test_insertar_correo_duplicado_falla(conn_test):
    """No debe permitirse insertar dos estudiantes con el mismo correo."""
    _insertar(conn_test, "Pedro", "mismo@test.com", "Arte")

    with pytest.raises(psycopg2.errors.UniqueViolation):
        with conn_test.cursor() as cur:
            cur.execute(
                "INSERT INTO estudiantes (nombre, correo, carrera) VALUES (%s, %s, %s);",
                ("Pablo", "mismo@test.com", "Musica"),
            )
        conn_test.commit()


def test_insertar_nombre_nulo_falla(conn_test):
    """El nombre es NOT NULL; insertar NULL debe lanzar NotNullViolation."""
    with pytest.raises(psycopg2.errors.NotNullViolation):
        with conn_test.cursor() as cur:
            cur.execute(
                "INSERT INTO estudiantes (nombre, correo, carrera) VALUES (%s, %s, %s);",
                (None, "sinNombre@test.com", "Sistemas"),
            )
        conn_test.commit()


# ── BUSCAR ───────────────────────────────────────────────────────────────────

def test_buscar_estudiante_existente(conn_test):
    """Buscar por nombre debe retornar el estudiante correcto."""
    _insertar(conn_test, "Carlos", "carlos@test.com", "Arquitectura")

    resultado = _buscar_por_nombre(conn_test, "Carlos")

    assert resultado is not None
    assert resultado.correo == "carlos@test.com"


def test_buscar_estudiante_inexistente(conn_test):
    """Buscar un estudiante que no existe debe retornar None."""
    resultado = _buscar_por_nombre(conn_test, "NoExiste")
    assert resultado is None


def test_buscar_por_correo(conn_test):
    """Buscar por correo debe encontrar exactamente ese estudiante."""
    _insertar(conn_test, "Laura", "laura@test.com", "Psicologia")

    resultado = _buscar_por_correo(conn_test, "laura@test.com")

    assert resultado is not None
    assert resultado.nombre == "Laura"


# ── is_equal ─────────────────────────────────────────────────────────────────

def test_is_equal_mismo_contenido():
    """Dos estudiantes con los mismos datos deben ser iguales."""
    e1 = Estudiante(nombre="Sofia", correo="sofia@test.com", carrera="Educacion")
    e2 = Estudiante(nombre="Sofia", correo="sofia@test.com", carrera="Educacion")
    assert e1.is_equal(e2) is True


def test_is_equal_diferente_contenido():
    """Dos estudiantes con datos distintos no deben ser iguales."""
    e1 = Estudiante(nombre="A", correo="a@test.com", carrera="X")
    e2 = Estudiante(nombre="B", correo="b@test.com", carrera="Y")
    assert e1.is_equal(e2) is False


def test_is_equal_no_es_estudiante():
    """is_equal debe retornar False si se compara con otro tipo de objeto."""
    e = Estudiante(nombre="A", correo="a@test.com", carrera="X")
    assert e.is_equal("no soy un estudiante") is False


# ── ACTUALIZAR ───────────────────────────────────────────────────────────────

def test_actualizar_nombre(conn_test):
    """Actualizar el nombre debe reflejarse al volver a consultar."""
    est = _insertar(conn_test, "Pedro", "pedro@test.com", "Quimica")

    with conn_test.cursor() as cur:
        cur.execute(
            "UPDATE estudiantes SET nombre = %s WHERE id = %s;",
            ("Pedro Actualizado", est.id),
        )
    conn_test.commit()

    resultado = _buscar_por_correo(conn_test, "pedro@test.com")
    assert resultado.nombre == "Pedro Actualizado"


def test_actualizar_carrera(conn_test):
    """Actualizar la carrera debe persistir correctamente."""
    est = _insertar(conn_test, "Maria", "maria@test.com", "Biologia")

    with conn_test.cursor() as cur:
        cur.execute(
            "UPDATE estudiantes SET carrera = %s WHERE id = %s;",
            ("Fisica", est.id),
        )
    conn_test.commit()

    resultado = _buscar_por_correo(conn_test, "maria@test.com")
    assert resultado.carrera == "Fisica"


def test_actualizar_estudiante_inexistente(conn_test):
    """Actualizar un ID que no existe no debe afectar ninguna fila."""
    with conn_test.cursor() as cur:
        cur.execute(
            "UPDATE estudiantes SET nombre = %s WHERE id = %s;",
            ("Fantasma", 99999),
        )
        filas_afectadas = cur.rowcount
    conn_test.commit()

    assert filas_afectadas == 0


# ── ELIMINAR ─────────────────────────────────────────────────────────────────

def test_eliminar_estudiante(conn_test):
    """Eliminar un estudiante debe hacer que deje de aparecer en consultas."""
    est = _insertar(conn_test, "Rosa", "rosa@test.com", "Enfermeria")

    with conn_test.cursor() as cur:
        cur.execute("DELETE FROM estudiantes WHERE id = %s;", (est.id,))
    conn_test.commit()

    resultado = _buscar_por_correo(conn_test, "rosa@test.com")
    assert resultado is None


def test_eliminar_estudiante_inexistente(conn_test):
    """Eliminar un ID que no existe no debe afectar ninguna fila."""
    with conn_test.cursor() as cur:
        cur.execute("DELETE FROM estudiantes WHERE id = %s;", (99999,))
        filas_afectadas = cur.rowcount
    conn_test.commit()

    assert filas_afectadas == 0
