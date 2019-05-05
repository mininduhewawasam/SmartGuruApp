import json
import random
import mysql.connector


def generaterandmQuiz():

    topicList = []
    questionList = []
    finalQuiz = []

    mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                              database='u2oI1tyJuT',
                                              user='u2oI1tyJuT',
                                              password='joBxFoudcl')

    select_topics_query = "select topic from questions group by topic"
    cursor1 = mySQLconnection.cursor()
    cursor1.execute(select_topics_query)
    topics = cursor1.fetchall()

    for topic in topics:
        topicList.append(topic[0])

    random_topics = []

    for i in random.sample(range(len(topicList)), 3):
        random_topics.append(topicList[i])

    print("------------------------------------")
    print("Random topics")
    print(random_topics)
    print("------------------------------------")

    for i in range(len(random_topics)):
        select_questions_query = "select * from questions where topic='" + random_topics[i] + "'"
        cursor2 = mySQLconnection.cursor()
        cursor2.execute(select_questions_query)
        questions = cursor2.fetchall()

        for rand_question in questions:

            answerList = []
            for i in range(7, 12):
                if rand_question[i] != "":
                    answerList.append(rand_question[i])

            questionList.append(
                {'qs_id': rand_question[0], 'qs_topic': rand_question[13], 'qs_chapter': rand_question[12],
                 'question': rand_question[1],
                 'options': {'op1': rand_question[2], 'op2': rand_question[3], 'op3': rand_question[4],
                             'op4': rand_question[5], 'op5': rand_question[6]}, 'answers': answerList,
                 'difficulty': rand_question[14]})


    if len(questionList) > 10:
        for i in random.sample(range(len(questionList)), 10):
            finalQuiz.append(questionList[i])

    return finalQuiz


def returnRandomQuiz():
    questions = generaterandmQuiz()
    while len(questions) < 10:
        questions = generaterandmQuiz()

    return json.dumps(questions)


