#!/usr/bin/python3
"""Script to list all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db_connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                    passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    # Create a cursor object to interact with the database
    db_cursor = db_connection.cursor()
    
    # Execute a query to select all states
    db_cursor.execute("SELECT * FROM states")
    
    # Fetch all rows from the result
    states_rows = db_cursor.fetchall()
    
    # Print each row
    for state_row in states_rows:
        print(state_row)
    
    # Close the cursor and database connection
    db_cursor.close()
    db_connection.close()

