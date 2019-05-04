from flask import Flask

import videosuggestions
import stacklinkssuggestions
import recQuizGenerator
import randQuestions
import addQuestionsToDB
import viewUsers
import SessionHandler


app = Flask(__name__)

@app.route('/youtubelinks')
def youtube():
    return videosuggestions.vediolinks()


@app.route('/stackoverflowlinks')
def stackoverflow():
    return stacklinkssuggestions.stacklinks()


@app.route('/recomand')
def recomendedQuiz():
    return recQuizGenerator.sendQuestions()


@app.route('/random')
def randomQuiz():
    return randQuestions.generaterandmQuiz()

@app.route('/addQS')
def addQuestions():
    return addQuestionsToDB.addQuestions()

@app.route('/users')
def showUsers():
    return viewUsers.displayUsers

@app.route('/login')
def login():
    return SessionHandler.login()

@app.route('/redirect')
def direct():
    return SessionHandler.redirect()

@app.route('/request')
def b_request():
    return SessionHandler.before_request()

@app.route('/getsession')
def get_session():
    return SessionHandler.getsession()

@app.route('/dropsession')
def drop_session():
    return SessionHandler.dropsession()


if __name__ == '__main__':
    app.run()
