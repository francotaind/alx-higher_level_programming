#!/usr/bin/python3

"""Module defining state class and base instance"""

import sqlalchemy
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = sqlalchemy.orm.declarative_base()

class State(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
