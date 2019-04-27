import questionSelector

import mysql.connector
from mysql.connector import Error

try:
    mySQLconnection = mysql.connector.connect(host='localhost',
                                              database='smartguru',
                                              user='root',
                                              password='')

    sql_select_Query = "select QuestionID,sessionID from sessionsdata where userID=2"
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        print(questionSelector.get_recommendations(row[0])[0])
    print("-------------------")
    for row in records:
        i = 0
        print(questionSelector.get_recommendations(row[0])[i+1])
    cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)

