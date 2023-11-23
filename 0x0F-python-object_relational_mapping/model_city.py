#!/usr/bin/python3
"""Defines a city class similar to airbnb cities class"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Defines a city class that inherits from Base"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
