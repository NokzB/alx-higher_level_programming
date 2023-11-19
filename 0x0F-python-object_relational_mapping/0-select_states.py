#!/usr/bin/python3
"""code to list all states from hbtn_0e_0_usa database"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
    my_cur = db.cursor()

    my_cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    rows = my_cur.fetchall()
    for row in rows:
        print(row)
    my_cur.close()
    db.close()
