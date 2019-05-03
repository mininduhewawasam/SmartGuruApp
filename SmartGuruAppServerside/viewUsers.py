import json

import mysql.connector
from mysql.connector import Error

userList = []
userList2 = []

def displayUsers():
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
                                'Password': row[3], 'User Type':row[4]})
        cursor.close()

        # count = 1
        # while count <= 10:
        #     # rand_question = random.choice(records)
        #
        #     answerList = rand_question[7].split(',')
        #     recQuizList.append({'qs_id': rand_question[0], 'qs_topic': rand_question[9], 'question': rand_question[1],
        #                         'options': {'op1': rand_question[2], 'op2': rand_question[3], 'op3': rand_question[4],
        #                                     'op4': rand_question[5], 'op5': rand_question[6]}, 'answers': answerList,
        #                         'difficulty': rand_question[10]})
        #
        #     count += 1

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        # closing database connection.
        if (mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")

    return json.dumps(userList)