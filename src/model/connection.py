import psycopg2

try:
    from secret_config import PG_HOST, PG_PORT, PG_DATABASE, PG_USER, PG_PASSWORD
except ImportError:
    raise RuntimeError(
        "No se encontró secret_config.py.\n"
        "Copia secret_config_sample.py, renómbralo secret_config.py "
        "y rellena tus credenciales de PostgreSQL."
    )


def get_connection():
    """Abre y retorna una conexión nueva a PostgreSQL."""
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        dbname=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD,
    )
