#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
            cur = db.cursor()
                cur.execute("SELECT * FROM `states`")
                    _states = cur.fetchall()
                        for state in _states:
                                    if state[1][0] == "N":
                                                    print(state)
