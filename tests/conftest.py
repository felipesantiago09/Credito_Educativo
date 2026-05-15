import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.model.connection import Base
from src.model.estudiante_model import Estudiante

TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def db_session():

    Base.metadata.create_all(engine)

    session = TestingSessionLocal()

    yield session

    session.close()

    Base.metadata.drop_all(engine)