import os
from flask import session, Flask
import mysql.connector
import json


def get_user_details(user_id):

    mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                              database='u2oI1tyJuT',
                                              user='u2oI1tyJuT',
                                              password='joBxFoudcl')

    sql_select_Query = "SELECT * FROM users WHERE userID='" + user_id + "'"
    cursor1 = mySQLconnection.cursor()
    cursor1.execute(sql_select_Query)
    user = cursor1.fetchone()

    print(json.dumps({"username": user[1], "email": user[2], "password": user[3]}))
    return json.dumps({"username": user[1], "email": user[2], "password": user[3]})


def update_user_details(user_id, data):

    SQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                              database='u2oI1tyJuT',
                                              user='u2oI1tyJuT',
                                              password='joBxFoudcl')

    response = json.loads(data)
    cursor = SQLconnection.cursor()
    sql = "UPDATE users SET userName = %s, userEmail = %s, password = %s WHERE userID = %s"
    val = (response.get("username"), response.get("email"), response.get("password"), user_id)
    cursor.execute(sql, val)
    SQLconnection.commit()


if __name__ == '__main__':
    get_user_details("saneth98")