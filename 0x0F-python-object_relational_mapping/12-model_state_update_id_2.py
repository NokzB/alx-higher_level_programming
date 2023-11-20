#!/usr/bin/python3
"""Script to update State objects from the database"""


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

    update_state = session.query(State).filter(State.id == '2').first()
    update_state.name = 'New Mexico'
    session.commit()
    session.close()
