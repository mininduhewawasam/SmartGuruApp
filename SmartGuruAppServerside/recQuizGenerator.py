from SmartGuruAppServerside import questionSelector
import json

import mysql.connector
from mysql.connector import Error

recQuizList=[]
recQuizList2=[]
sentjson=json
try:
    mySQLconnection = mysql.connector.connect(host='localhost',
                                              database='smartguru',
                                              user='root',
                                              password='')

    sql_select_Query = "select QuestionID,sessionID from sessionsdata where userID=2"
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    # sql_select_Query2 = "select * from questions where questionID=1"
    # cursor2 = mySQLconnection.cursor()
    # cursor2.execute(sql_select_Query2)
    # records2 = cursor.fetchall()

    # print("SELECT questions.question FROM questions INNER JOIN sessionsdata on sessionsdata.QuestionID=questions.questionID WHERE sessionsdata.userID=2;")

    for row in records:
        # print(questionSelector.get_recommendations(row[0])[0])
        #
        # print("-------------------")



        sql_select_Query2 = "select * from questions where questionID="+str(questionSelector.get_recommendations(row[0])[0])+""
        cursor2 = mySQLconnection.cursor()
        cursor2.execute(sql_select_Query2)
        records2 = cursor2.fetchall()

        recQuizList.append(records2)



except Error as e:
    print("Error while connecting to MySQL", e)

def sendQuestions():
    try:
        mySQLconnection = mysql.connector.connect(host='localhost',
                                                  database='smartguru',
                                                  user='root',
                                                  password='')

        sql_select_Query = "select QuestionID,sessionID from sessionsdata where userID=2"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        # sql_select_Query2 = "select * from questions where questionID=1"
        # cursor2 = mySQLconnection.cursor()
        # cursor2.execute(sql_select_Query2)
        # records2 = cursor.fetchall()

        # print("SELECT questions.question FROM questions INNER JOIN sessionsdata on sessionsdata.QuestionID=questions.questionID WHERE sessionsdata.userID=2;")

        for row in records:
            #print(questionSelector.get_recommendations(row[0])[0])

            # print("-------------------")

            sql_select_Query2 = "select * from questions where questionID=" + str(
                questionSelector.get_recommendations(row[0])[0])+""
            cursor2 = mySQLconnection.cursor()
            cursor2.execute(sql_select_Query2)
            records2 = cursor2.fetchall()

            recQuizList.append(records2)
            # sentjson = json.dumps({'q_id': row[0][0], 'question': row[0][1]})


        for row2 in recQuizList:
            print(row2[0][0])
            print(row2[0][1])
            print("----------")

            recQuizList2.append({'q_id':row2[0][0], 'question':row2[0][1]})

    except Error as e:
        print("Error while connecting to MySQL", e)

    print(recQuizList[0][0][8])

    return json.dumps(recQuizList2)


print(sendQuestions())


