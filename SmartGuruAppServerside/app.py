from flask import Flask
# from SmartGuruAppServerside import generaterandmQuiz
from SmartGuruAppServerside import recQuizGenerator
from SmartGuruAppServerside import randQuestions

app = Flask(__name__)


@app.route('/recomand')
def recomendedQuiz():
    return recQuizGenerator.sendQuestions()


@app.route('/random')
def randomQuiz():
    return randQuestions.generaterandmQuiz()



if __name__ == '__main__':
    app.run()
