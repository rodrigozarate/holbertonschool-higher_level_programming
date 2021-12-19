#!/usr/bin/python3
""" Simple list of table states filtered by initial N """

import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    holder = connection.cursor()
    userInput = sys.argv[4]
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC"\
    .format(userInput)
    holder.execute(query)
    rows = holder.fetchall()
    for row in rows:
        print(row)
    holder.close()
    connection.close()
