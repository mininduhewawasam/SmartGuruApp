from flask import Flask

app = Flask(__name__)


@app.route('/login')
def hello_world():
    return 'Hello World!ssss'


if __name__ == '__main__':
    app.run()
