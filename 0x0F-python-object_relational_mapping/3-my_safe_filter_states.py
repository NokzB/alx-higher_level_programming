#!/usr/bin/python3
"""code to list all states from hbtn_0e_0_usa database"""

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
    with db.cursor() as my_cur:
        my_cur.execute("""
                SELECT
                    *
                FROM
                    states
                WHERE
                    name LIKE BINARY %(name)s
                ORDER BY
                    states.id ASC
        """, {
            'name': argv[4]
        })
        rows = my_cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
