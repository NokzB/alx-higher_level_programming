#!/usr/bin/python3
"""Script to list all State objects from the database"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """Accesses the database to get the states"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == argv[4]).first()

    if instance is None:
        print("Not found")
    else:
        print('{0}'.format(instance.id))
