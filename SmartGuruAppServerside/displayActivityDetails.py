import json

import mysql.connector
from mysql.connector import Error

userList = []
userList2 = []

def displayActivity():
    userList.clear()

    try:
        mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                              database='u2oI1tyJuT',
                                              user='u2oI1tyJuT',
                                              password='joBxFoudcl')
        sql_select_Query = "select * from users"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        print("Total number of rows in python_developers is - ", cursor.rowcount)
        print("Printing each row's column values i.e.  developer record")

        for row in records:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Email  = ", row[2])
            print("Password  = ", row[3])
            print("usertype = ", row[4], "\n")

            userList.append({'Id': row[0], 'Name': row[1], 'Email': row[2],
                                'Password': row[3], 'UserType':row[4]})
        cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        # closing database connection.
        if (mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")

    return json.dumps(userList)