import mysql.connector
from mysql.connector import Error
import datetime
import json


def db_connection():
    return mysql.connector.connect(host='www.remotemysql.com',
                                             database='u2oI1tyJuT',
                                             user='u2oI1tyJuT',
                                             password='joBxFoudcl')


def create_quiz_session(total_qs, total_correct_qs):

    sql_connection = db_connection()
    sql_query = 'INSERT INTO sessionsdetails (userID, dateTime, quizChapter, totalQs, correctQsTotal) VALUES (%s, %s, %s, %s, %s)'
    now = datetime.datetime.now()
    val = (1, now, "Mix", total_qs, total_correct_qs)
    cursor = sql_connection.cursor()
    cursor.execute(sql_query, val)
    sql_connection.commit()
    cursor.close()


def get_created_session_id():
    sql_connection = db_connection()
    sql_select_query = 'select max(sessionID) from sessionsdetails where userID="' + str(1) + '"'
    cursor = sql_connection.cursor()
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    return record[0]


def add_wrong_question_ids(questions):

    val = []

    sql_connection = db_connection()

    #qs_data = response.get("wrong_qs")
    for qs in questions:
        qs_id = qs.get('qsId')
        qs_topic = qs.get('qsTopic')

        val.append((get_created_session_id(), 1, qs_id, qs_topic))

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


def update_mixed_quiz_table(chapter_scores):

    val = []
    sql_conn = db_connection()
    insert_query = 'INSERT INTO mixedquizdata (sessionID, chapter, totalQs, correctQsTotal) VALUES (%s, %s, %s, %s)'
    for chapter_score in chapter_scores:
        val.append((get_created_session_id(), chapter_score.get("chapter"), chapter_score.get("total_qs"), chapter_score.get("correct_qs")))

    cursor = sql_conn.cursor()
    cursor.executemany(insert_query, val)
    sql_conn.commit()
    cursor.close()


def update_quiz_results(data):

    response = json.loads(data)

    print(response.get("total_qs"))
    create_quiz_session(response.get("total_qs"), response.get("total_correct_qs"))
    add_wrong_question_ids(response.get("wrong_qs"))
    update_mixed_quiz_table(response.get("chapter_scores"))


