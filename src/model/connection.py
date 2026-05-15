from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

# Leer DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Conexion PostgreSQL
engine = create_engine(DATABASE_URL)

# Sesion ORM
Session = sessionmaker(bind=engine)

# Base para modelos
Base = declarative_base()