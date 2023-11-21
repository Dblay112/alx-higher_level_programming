#!/usr/bin/python3
"""modules
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 5:
        print("Usage: {} username password db_name state_name".format(args[0]))
        exit(1)

    # connect to database and set up user input variables
    username = args[1]
    password = args[2]
    data = args[3]
    statename = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data,
                         port=3306)
    cur = db.cursor()
    
    data_rows = cur.execute('''
        SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON cities.state_id=states.id
        ORDER BY cities.id ASC
        ''')
    rows = cur.fetchall()
    
    cities = [row[1] for row in rows if statename == row[2]]
    data_cities = len(cities)
    
    for i, city in enumerate(cities):
        if i == data_cities - 1:
            print(city)
        else:
            print(city, end=", ")
