from flask import Flask
# from SmartGuruAppServerside import generaterandmQuiz
import recQuizGenerator
import randQuestions
import addQuestionsToDB
import viewUsers

app = Flask(__name__)


@app.route('/.')
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
    return viewUsers.displayUsers()


if __name__ == '__main__':
    app.run()
