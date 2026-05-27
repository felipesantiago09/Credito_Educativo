import pytest
import psycopg2

try:
    from secret_config import PG_HOST, PG_PORT, PG_DATABASE, PG_USER, PG_PASSWORD
except ImportError:
    raise RuntimeError(
        "Necesitas secret_config.py con tus credenciales de PostgreSQL para correr los tests."
    )

# Base de datos de prueba separada — NUNCA uses la base de datos de producción
TEST_DB = PG_DATABASE + "_test"


def _get_conn(dbname=None):
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        dbname=dbname or PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD,
    )


def _crear_base_test():
    """Crea la base de datos de test si no existe."""
    conn = _get_conn()
    conn.autocommit = True
    try:
        with conn.cursor() as cur:
            cur.execute(f"SELECT 1 FROM pg_database WHERE datname = %s;", (TEST_DB,))
            if not cur.fetchone():
                cur.execute(f'CREATE DATABASE "{TEST_DB}";')
    finally:
        conn.close()


def _get_conn_test():
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        dbname=TEST_DB,
        user=PG_USER,
        password=PG_PASSWORD,
    )


@pytest.fixture(scope="function")
def conn_test():
    """
    Fixture que entrega una conexión a la base de datos de TEST.
    Crea la tabla antes de cada test y la borra al terminar.
    """
    _crear_base_test()
    conn = _get_conn_test()

    # Crear tabla limpia
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

    yield conn

    # Limpiar al terminar
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS estudiantes;")
    conn.commit()
    conn.close()
