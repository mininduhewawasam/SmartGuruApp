from flask import session
import mysql.connector
import json


def register_user(data):

    mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                              database='u2oI1tyJuT',
                                              user='u2oI1tyJuT',
                                              password='joBxFoudcl')

    user_details = json.loads(data)

    username = user_details.get("username")
    email = user_details.get("email")
    password = user_details.get("password")
    user_type = user_details.get("userType")

    sql_select_Query = "SELECT * FROM users WHERE userName='" + username + "' or userEmail='"+email+"'"
    cursor1 = mySQLconnection.cursor()
    cursor1.execute(sql_select_Query)
    records = cursor1.fetchall()


    if len(records) == 0:
        sql_query = 'INSERT INTO users (userName, userEmail, password, userType) VALUES (%s, %s, %s, %s)'
        cursor = mySQLconnection.cursor()
        val = (username, email, password, user_type)
        cursor.execute(sql_query, val)
        mySQLconnection.commit()

        session['user'] = username

        return json.dumps({"status": "Successfully Registered"})
    else:
        return json.dumps({"status": "User Already Exist"})