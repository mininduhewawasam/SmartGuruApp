from flask import Flask, request, session, render_template, g, app
import os
import mysql.connector
from mysql.connector import Error
from pandas._libs import json
from werkzeug.security import generate_password_hash



try:
    mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                              database='u2oI1tyJuT',
                                              user='u2oI1tyJuT',
                                             password='joBxFoudcl')


except Error as e:
    print("Error while connecting to MySQL", e)



def showSignUp():
   return render_template('signup.html')


#@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        _username = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _username and _email and _password:

            # All Good, let's call MySQL

            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser', (_username, _email, _hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()


