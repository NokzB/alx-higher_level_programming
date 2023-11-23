#!/usr/bin/python3
"""Prints all city objects from the database"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """accessing the database to get the cities"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()
    query = session.query(City, State).join(State)

    for cit, sta in query.all():
        print("{}: ({:d}) {}".format(sta.name, cit.id, cit.name))

    session.commit()
    session.close()
