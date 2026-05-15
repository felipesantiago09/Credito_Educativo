from src.model.estudiante_model import Estudiante


# =========================
# INSERTAR
# =========================

def test_insertar_estudiante(db_session):

    estudiante = Estudiante(
        nombre="Juan",
        correo="juan@test.com",
        carrera="Ingenieria"
    )

    db_session.add(estudiante)
    db_session.commit()

    resultado = db_session.query(Estudiante).filter_by(
        correo="juan@test.com"
    ).first()

    assert resultado is not None
    assert resultado.nombre == "Juan"


def test_insertar_varios_estudiantes(db_session):

    e1 = Estudiante(
        nombre="Ana",
        correo="ana@test.com",
        carrera="Medicina"
    )

    e2 = Estudiante(
        nombre="Luis",
        correo="luis@test.com",
        carrera="Derecho"
    )

    db_session.add_all([e1, e2])

    db_session.commit()

    resultado = db_session.query(Estudiante).all()

    assert len(resultado) == 2


def test_insertar_nombre_obligatorio(db_session):

    estudiante = Estudiante(
        nombre=None,
        correo="error@test.com",
        carrera="Sistemas"
    )

    try:
        db_session.add(estudiante)
        db_session.commit()
        assert False

    except Exception:
        assert True


# =========================
# BUSCAR
# =========================

def test_buscar_estudiante(db_session):

    estudiante = Estudiante(
        nombre="Carlos",
        correo="carlos@test.com",
        carrera="Arquitectura"
    )

    db_session.add(estudiante)
    db_session.commit()

    resultado = db_session.query(Estudiante).filter_by(
        nombre="Carlos"
    ).first()

    assert resultado is not None


def test_buscar_estudiante_inexistente(db_session):

    resultado = db_session.query(Estudiante).filter_by(
        nombre="NoExiste"
    ).first()

    assert resultado is None


def test_listar_estudiantes(db_session):

    e1 = Estudiante(
        nombre="A",
        correo="a@test.com",
        carrera="A"
    )

    e2 = Estudiante(
        nombre="B",
        correo="b@test.com",
        carrera="B"
    )

    db_session.add_all([e1, e2])

    db_session.commit()

    resultado = db_session.query(Estudiante).all()

    assert len(resultado) == 2


# =========================
# ACTUALIZAR
# =========================

def test_actualizar_estudiante(db_session):

    estudiante = Estudiante(
        nombre="Pedro",
        correo="pedro@test.com",
        carrera="Quimica"
    )

    db_session.add(estudiante)
    db_session.commit()

    estudiante.nombre = "Pedro Actualizado"

    db_session.commit()

    resultado = db_session.query(Estudiante).filter_by(
        correo="pedro@test.com"
    ).first()

    assert resultado.nombre == "Pedro Actualizado"


def test_actualizar_carrera(db_session):

    estudiante = Estudiante(
        nombre="Maria",
        correo="maria@test.com",
        carrera="Biologia"
    )

    db_session.add(estudiante)
    db_session.commit()

    estudiante.carrera = "Fisica"

    db_session.commit()

    resultado = db_session.query(Estudiante).filter_by(
        correo="maria@test.com"
    ).first()

    assert resultado.carrera == "Fisica"


def test_actualizar_estudiante_inexistente(db_session):

    resultado = db_session.query(Estudiante).filter_by(
        nombre="Fantasma"
    ).first()

    assert resultado is None