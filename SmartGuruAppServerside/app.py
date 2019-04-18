from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!ssss4'


if __name__ == '__main__':
    app.run()
