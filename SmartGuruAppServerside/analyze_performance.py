import mysql.connector
from mysql.connector import Error
import json
import datetime

all_questions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
correct_answer_total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

chapter_names = [
        "Introduction to Computers, Programs, and Java",
        "Elementary Programming",
        "Selections",
        "Loops",
        "Methods",
        "Single-Dimensional Arrays",
        "Objects and Classes",
        "Strings",
        "Thinking in Objects",
        "Inheritance and Polymorphism"

    ]


def add_wrong_questions(data):

    response = json.loads(data)

    print(response)

    sql_connection = mysql.connector.connect(host='www.remotemysql.com',
                                             database='u2oI1tyJuT',
                                             user='u2oI1tyJuT',
                                             password='joBxFoudcl')
    val = []

    #global data

    create_quiz_session(response.get("chapter"), response.get("quiz_level"), response.get("total_qs"), response.get("total_wrong_qs"))
    sql_select_query = 'select max(sessionID) from sessionsdetails where userID="' + str(1) + '"'
    cursor = sql_connection.cursor()
    cursor.execute(sql_select_query)
    record = cursor.fetchone()

    print(record[0])

    qs_data = response.get("wrong_qs")
    for qs in qs_data:
        qs_id = qs.get('qsId')
        qs_topic = qs.get('qsTopic')

        val.append((record[0], 1, qs_id, qs_topic))

    try:



        sql_query = 'INSERT INTO sessionsdata (sessionID, userID, QuestionID, QuestionTopic) VALUES (%s, %s, %s, %s)'
        cursor = sql_connection.cursor()
        cursor.executemany(sql_query, val)
        sql_connection.commit()
        cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        val.clear()
        if sql_connection.is_connected():
            sql_connection.close()
            print("MySQL connection is closed")


def create_quiz_session(chapter, level, total_qs, total_wrong_qs):
    sql_connection = mysql.connector.connect(host='www.remotemysql.com',
                                             database='u2oI1tyJuT',
                                             user='u2oI1tyJuT',
                                             password='joBxFoudcl')

    sql_query = 'INSERT INTO sessionsdetails (userID, dateTime, quizChapter, quizLevel, totalQs, correctQsTotal) VALUES (%s, %s, %s, %s, %s, %s)'
    now = datetime.datetime.now();
    val = (1, now, chapter, level, total_qs, total_wrong_qs)
    cursor = sql_connection.cursor()
    cursor.execute(sql_query, val)
    sql_connection.commit()
    cursor.close()


def calculate_performance(user_id):

    global all_questions
    global correct_answer_total

    sql_connection = mysql.connector.connect(host='www.remotemysql.com',
                                             database='u2oI1tyJuT',
                                             user='u2oI1tyJuT',
                                             password='joBxFoudcl')

    quiz_data = []

    try:

        a = "SELECT * FROM sessionsdetails WHERE userID='" + user_id + "'"
        sql_query = a
        cursor = sql_connection.cursor()
        cursor.execute(sql_query)
        records = cursor.fetchall()

        if len(records) != 0:

            for row in records:

                if row[3] == "Mix":
                    calculate_mixed_quiz_performance(row[0])
                    print("Mix")
                else:
                    for i in range(10):
                        if row[3] == chapter_names[i]:
                            all_questions[i] += row[5]
                            correct_answer_total[i] += row[6]

            for i in range(len(chapter_names)):
                if all_questions[i] != 0:
                    quiz_data.append(
                        {"chapter": chapter_names[i], "chapterScore": int((correct_answer_total[i]/all_questions[i])*100)})
                else:
                    quiz_data.append(
                        {"chapter": chapter_names[i], "chapterScore": 0})
        cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if sql_connection.is_connected():
            sql_connection.close()
            print("MySQL connection is closed")
        print(json.dumps(quiz_data))
        return json.dumps({"scores": quiz_data})


def calculate_mixed_quiz_performance(session_id):

    global all_questions
    global correct_answer_total

    sql_connection = mysql.connector.connect(host='www.remotemysql.com',
                                             database='u2oI1tyJuT',
                                             user='u2oI1tyJuT',
                                             password='joBxFoudcl')

    try:

        sql_query = 'select * from mixedquizdata where sessionID = "' + str(session_id) + '"'
        cursor = sql_connection.cursor()
        cursor.execute(sql_query)
        records = cursor.fetchall()

        if len(records) != 0:

            for row in records:

                for i in range(10):
                    if row[1] == chapter_names[i]:
                        all_questions[i] += row[2]
                        correct_answer_total[i] += row[3]

        cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if sql_connection.is_connected():
            sql_connection.close()
            print("MySQL connection is closed")
