from .config import Settings
from .crud.log import Log
from psycopg2 import errors as dbError# https://www.psycopg.org/docs/errors.html

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


POSTGRES_URL = Settings.psql_url

# def connection():
#     try:
#         con = psycopg2.connect(POSTGRES_URL)
#         con.set_session(autocommit=True)
#     except dbError.CannotConnectNow:
#         raise dbError
#     return con

engine = create_engine(POSTGRES_URL, pool_pre_ping=True, echo=True)

Session = sessionmaker(autocommit=False, autoflush= False, bind=engine)

Base = declarative_base()

from api.models.log import Log

