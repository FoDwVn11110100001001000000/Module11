import configparser

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('config.ini')

user = config.get('DATABASE', 'USER')
password = config.get('DATABASE', 'PASSWORD')
host = config.get('DATABASE', 'HOST')
port = config.get('DATABASE', 'PORT')
name = config.get('DATABASE', 'NAME')

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    email = Column(String(150),unique=True, nullable=False)
    phone = Column(String(20),unique=True,nullable=False)
    birthday = Column(Date,nullable=False)
    notes = Column(String(500),nullable=True)


Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()