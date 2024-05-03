#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class that defines each city.
    """
    __tablename__ = 'cities'
    identifier = Column(Integer, unique=True, nullable=False, primary_key=True)
    city_name = Column(String(128), nullable=False)
    state_identifier = Column(Integer, ForeignKey("states.id"), nullable=False)
