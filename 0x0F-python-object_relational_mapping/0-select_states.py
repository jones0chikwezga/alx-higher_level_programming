#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows in the result of the query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # List states from the database
    list_states(username, password, database)
