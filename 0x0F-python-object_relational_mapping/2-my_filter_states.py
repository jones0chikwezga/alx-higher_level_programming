#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa which match name
    passed as argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` \
                WHERE BINARY name = '{}'".format(sys.argv[4]))
    _states = cur.fetchall()
    for state in _states:
        print(state)
