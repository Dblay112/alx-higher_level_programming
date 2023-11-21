#!/usr/bin/python3
"""
modules imported
"""
import sys
import MySQLdb


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    user = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=password, db=data,
                         port=3306)
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
