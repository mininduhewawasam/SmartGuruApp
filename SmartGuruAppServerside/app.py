from flask import Flask
from SmartGuruApp import generaterandmQuiz
from SmartGuruApp import sendQuestions

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return sendQuestions()


@app.route('/random')
def hello_world():
    return generaterandmQuiz()



if __name__ == '__main__':
    app.run()
