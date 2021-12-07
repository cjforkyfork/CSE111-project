import sqlite3
from sqlite3 import Error
from flask import jsonify

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    try:

        cursor = _conn.cursor()
        query = '''
        SELECT customer_id, customer_name
        FROM customer 
        WHERE customer_id = ?
        '''
        c_key = str(11)
        c_name = 'Jorge Brian Gonzalez	'
        
        args = [c_key]

        cursor.execute(query,args)
        rows = cursor.fetchall()
        rows2 = cursor.fetchone()
        print(rows)
        print(rows2)
        # if rows[0][0] == None and rows[0][1] == None:
        #         print('here')
        
        
        
        # print((rows[0][1]))
        
            

        
        
        
        

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"animals.db"

    # create a database connection
    conn = openConnection(database)
    with conn:
        Q1(conn)
    closeConnection(conn, database)


if __name__ == '__main__':
    main()


