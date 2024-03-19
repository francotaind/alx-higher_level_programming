#!/usr/bin/python3

"""Script that lists all objects from a database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}'
        f'@localhost:3306/{sys.argv[3]}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).first()
    if not states:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
