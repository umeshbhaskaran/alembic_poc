
#Required only for standalone implementation
import os
import sys


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from alembic_poc.config.config import Config

class Database(object):
    """Initializes DB engine, creates connection and corresponding session."""

    def __init__(self):
        self.engine = create_engine(
            Config.DB_DIALECT+"://"+
            Config.DB_USERNAME+":"+
            Config.DB_PASSWORD+"@"+
            Config.DB_HOST+"/"+
            Config.DB_NAME,
            echo=False)
        self.engine.connect()
        self.base = declarative_base()
        self.sm = sessionmaker(bind=self.engine)
        self.session = self.sm()
        self.base.metadata.bind = self.engine

#Object creation - just for testing purpose
db = Database()
