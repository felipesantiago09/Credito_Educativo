from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///credito.db"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

session = Session()