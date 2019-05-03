from SmartGuruAppServerside import questionSelector
import json

import mysql.connector
from mysql.connector import Error

recQuizList = []
recQuizList2 = []
sentjson = json


def sendQuestions():
    recQuizList2.clear()
    recQuizList.clear()
    try:

        mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                                  database='u2oI1tyJuT',
                                                  user='u2oI1tyJuT',
                                                  password='joBxFoudcl')

        # mySQLconnection = mysql.connector.connect(host='Localhost',
        #                                           database='smartgurunew',
        #                                           user='root',
        #                                           password='')

        sql_select_Query = "SELECT questionID FROM sessionsdata WHERE userID=1 ORDER BY questionID DESC LIMIT 10"
        cursor1 = mySQLconnection.cursor()
        cursor1.execute(sql_select_Query)
        records = cursor1.fetchall()
        # print(records)
        # print("SELECT questionID FROM sessionsdata WHERE userID=1 ORDER BY questionID DESC LIMIT 2")


        for row in records:
            sql_select_Query2 = "select * from user where questionID=" + str(
                questionSelector.get_recommendations(row[0])[0])+""
            cursor2 = mySQLconnection.cursor()
            cursor2.execute(sql_select_Query2)
            records2 = cursor2.fetchall()
            recQuizList.append(records2)
            # print(records2)

        for row2 in recQuizList:
            # print(row2[0][0])
            answerList = row2[0][7].split(',')

            recQuizList2.append({'qs_id': row2[0][0], 'qs_topic': row2[0][9], 'question': row2[0][1], 'options': {'op1': row2[0][2], 'op2': row2[0][3], 'op3': row2[0][4], 'op4': row2[0][5], 'op5': row2[0][6]}, 'answers': answerList,   'difficulty': row2[0][10]})

    except Error as e:
        print("Error while connecting to MySQL", e)

    return json.dumps(recQuizList2)



