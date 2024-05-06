#!/usr/bin/python3
"""Print the State object with the name passed as an argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessiomaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database name> <state name<".format(sys.argv[0]))
        sys.exit(1)

        # Connect to the MySQL server
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the State object with the given name
        state_name = sys.argv[4]
        state = session.query(State).filter(State.name == state_name).first()

        # Print the state ID if found, otherwise print "Not found"
        if state:
            print(state.id)
        else:
            print("Not found")

        # Close the session
        session.close()
