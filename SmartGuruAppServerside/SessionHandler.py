from flask import Flask,request,session,render_template,g
import os
import mysql.connector
from mysql.connector import Error

try:
    mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
                                              database='u2oI1tyJuT',
                                              user='u2oI1tyJuT',
                                             password='joBxFoudcl')


except Error as e:
    print("Error while connecting to MySQL", e)


def login():
    if request.method == 'POST':
       session.pop('user', None)

       username=request.form['username']

       sql_select_Query = "SELECT * FROM users WHERE userName='"+username+"'"
       cursor1 = mySQLconnection.cursor()
       cursor1.execute(sql_select_Query)
       records = cursor1.fetchall()

       if request.form['password'] == (records[0][3]):
           session['user'] = request.form['username']
           return "USer logged Successfully! \n TODO:Load to homepage"

    return render_template('index.html')


def redirect():
   if g.user:
     return render_template('protected.html')

   return  render_template('index.html')

def before_request():
    g.user = None
    if 'user' in session:
     g.user = session['user']


def getsession():
   if 'user' in session:
     return session['user']

   return  'not logged in'


def dropsession():
   session.pop('user', None)
   return 'Dropped!'

