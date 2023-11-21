#!/usr/bin/python3
"""modules used in getting all states from sql db
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    username = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data,
                         port=3306)
    my_cur = db.cursor()
    num_rows = my_cur.execute('''
            SELECT * FROM states
            WHERE states.name LIKE 'N%'
            ORDER BY states.id
            ''')
    rows = my_cur.fetchall()
    for row in rows:
        print(row)