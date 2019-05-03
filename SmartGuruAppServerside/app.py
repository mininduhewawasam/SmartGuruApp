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
def youtube():
    return SessionHandler.login()



if __name__ == '__main__':
    app.run()
