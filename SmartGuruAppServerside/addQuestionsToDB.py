import json
import random
import mysql.connector
recQuizList = []

def addQuestions():
    recQuizList.clear()

    mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                              database='u2oI1tyJuT',
                                              user='u2oI1tyJuT',
                                              password='joBxFoudcl')

    sql_select_Query = "INSERT INTO questions (`questionID`, `question`, `a1`, `a2`, `a3`, `a4`, `a5`, `correctanswer`, `chapter`, `topic`, `difficulty`) VALUES ('', '', '', '', '', '', '', '', '', '', '')"
    cursor1 = mySQLconnection.cursor()
    cursor1.execute(sql_select_Query)
    records = cursor1.fetchall()

    count = 1
    while count <= 10:
        rand_question = random.choice(records)

        answerList = rand_question[7].split(',')
        recQuizList.append({'qs_id': rand_question[0], 'qs_topic': rand_question[9], 'question': rand_question[1],
                            'options': {'op1': rand_question[2], 'op2': rand_question[3], 'op3': rand_question[4],
                                        'op4': rand_question[5], 'op5': rand_question[6]}, 'answers': answerList,
                            'difficulty': rand_question[10]})

        count += 1

    return "Class and Method created. Add questions to Database."