from flask import Flask
from SmartGuruAppServerside import recQuizGenerator

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return recQuizGenerator.sendQuestions()


if __name__ == '__main__':
    app.run()
