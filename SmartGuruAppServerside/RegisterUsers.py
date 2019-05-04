from flask import Flask,request,session,render_template,g
import os
import mysql.connector
from mysql.connector import Error
from pandas._libs import json
from werkzeug.security import generate_password_hash

app = Flask(__name__)