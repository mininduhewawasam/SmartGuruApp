import mysql.connector
from mysql.connector import Error
import json



class Question:

    def __init__(self, qs_id, qs_topic, question, options, answers, difficulty_level):
        self.qs_id = qs_id
        self.qs_topic = qs_topic
        self.question = question
        self.options = options
        self.answers = answers
        self.difficulty = difficulty_level


class Options:

    def __init__(self, op1, op2, op3, op4, op5):
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.op5 = op5


def get_questions(lesson, level):

    qs_list = []

    try:

        sql_connection = mysql.connector.connect(host='www.remotemysql.com',
                                                 database='u2oI1tyJuT',
                                                 user='u2oI1tyJuT',
                                                 password='joBxFoudcl')

        sql_query = 'select * from questions where chapter = "'+lesson+'" and difficulty="'+level+'"'
        cursor = sql_connection.cursor()
        cursor.execute(sql_query)
        records = cursor.fetchall()
        print("Total number of rows in questions is - ", cursor.rowcount)
        print("Printing each row's column values i.e.  developer record")
        for row in records:
            options = Options(row[2], row[3], row[4], row[5], row[6])
            #ans = row[7].split(",")
            ans = []
            for i in range(7, 12):
                if row[i]!="":
                    ans.append(row[i])
            qs = Question(row[0], row[13], row[1], options.__dict__, ans, row[14])
            qs_list.append(qs.__dict__)
        cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if sql_connection.is_connected():
            sql_connection.close()
            print("MySQL connection is closed")

    print(qs_list)
    return json.dumps(qs_list)


if __name__ == '__main__':
    get_questions('Introduction to Computers, Programs, and Java', 'easy')
