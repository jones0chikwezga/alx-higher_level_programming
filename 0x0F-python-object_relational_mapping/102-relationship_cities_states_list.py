#!/usr/bin/python3
"""script that lists all State objects from the given database"""
import sys
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                   .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                                                              pool_pre_ping=True)
                                                                  Session = sessionmaker(bind=engine)
                                                                      session = Session()
                                                                          states = session.query(State).order_by(State.id)
                                                                              for state in states:
                                                                                      for city in state.cities:
                                                                                                  print("{}: {} -> {}".format(city.id, city.name, state.name))
