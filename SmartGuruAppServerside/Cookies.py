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

def getsession():
   if 'user' in session:
     return session['user']

   return  'not logged in'


def dropsession():
   session.pop('user', None)
   return 'Dropped!'
