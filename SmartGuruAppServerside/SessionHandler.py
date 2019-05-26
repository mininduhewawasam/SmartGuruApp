from flask import session
import mysql.connector
import json


def user_login(data):

    mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                              database='u2oI1tyJuT',
                                              user='u2oI1tyJuT',
                                              password='joBxFoudcl')

    user_details = json.loads(data)

    username = user_details.get("username")
    password = user_details.get("password")

    sql_select_Query = "SELECT * FROM users WHERE userName='" + username + "'"
    cursor1 = mySQLconnection.cursor()
    cursor1.execute(sql_select_Query)
    records = cursor1.fetchall()

    if len(records) == 0:
        return json.dumps({"status": "User Doesn't Exist"})
    else:
        if password == (records[0][3]):
            return json.dumps({"status": "Access Allowed", "userID": records[0][0], "userType": records[0][4]})
        else:
            return json.dumps({"status": "Incorrect Password"})
