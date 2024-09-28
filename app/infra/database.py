from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'posgresql://postgres:Avance2025@localhost:5432/avance'

engine = create_engine(URL_DATABASE)

SessionLocal =  sessionmaker(autocomit=False, autoflush=False, bind=engine)

Base = declarative_base()