from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://adminesteban_y_felipe:20uOvMkWmwxQyKgUwckPmGmvggeEkH1f@dpg-d81jsecvikkc73a5rgjg-a.oregon-postgres.render.com:5432/credito_db"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

Base = declarative_base()