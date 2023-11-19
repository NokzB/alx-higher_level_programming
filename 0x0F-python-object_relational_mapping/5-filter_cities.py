#!/usr/bin/python3
"""code to list all cities from states_id from hbtn_0e_0_usa database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    my_cur = db.cursor()

    my_cur.execute("""SELECT cities.name FROM
                    cities INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s""", (argv[4],))

    rows = my_cur.fetchall()

    if rows is not None:
        print(", ".join([row[0] for row in rows]))
        my_cur.close()
        db.close()
