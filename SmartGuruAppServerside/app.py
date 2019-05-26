from flask import Flask, jsonify, request, session

import videosuggestions
import stacklinkssuggestions
import recQuizGenerator
import randQuestions
import addQuestionsToDB
import viewUsers
import SessionHandler as login
import RegisterUsers as register
import analyze_performance as analyzer
import quiz_result_handler as quiz_handler
import lesson_quiz_generator
import leaderboard
import edit_profile as profile


app = Flask(__name__)


@app.route('/youtubelinks/<string:user_id>')
def youtube(user_id):
    return videosuggestions.vediolinks(user_id)


@app.route('/stackoverflowlinks/<string:user_id>')
def stackoverflow(user_id):
    return stacklinkssuggestions.stacklinks(user_id)


@app.route('/leaderboardlist')
def leaderboardmarks():
    return leaderboard.sortedmarks()


@app.route('/recomand/<string:user_id>')
def recomendedQuiz(user_id):
    return recQuizGenerator.sendQuestions(user_id)


@app.route('/lessons/<string:level>/<string:lesson>')
def get_questions(lesson, level):
    return lesson_quiz_generator.get_questions(lesson, level)


@app.route('/performance/<string:user_id>', methods=['GET'])
def get_performance(user_id):
    return analyzer.calculate_performance(user_id)


@app.route('/random')
def randomQuiz():
    return randQuestions.returnRandomQuiz()

@app.route('/addQS')
def addQuestions():
    return addQuestionsToDB.addQuestions()

@app.route('/users')
def showUsers():
    return viewUsers.displayUsers()


@app.route('/login', methods=['POST'])
def login():
    data = request.data
    return login.user_login(data)


@app.route('/signup', methods=['POST'])
def user_register():
    data = request.data
    return register.register_user(data)

@app.route('/edit/<string:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
    if request.method == "GET":
        return profile.get_user_details(user_id)
    if request.method == "POST":
        data = request.data
        return profile.update_user_details(user_id, data)


@app.route('/quiz', methods=['POST'])
def get_wrong_answers():
    data = request.data
    analyzer.add_wrong_questions(data)
    return jsonify({
        'status': 'ok'
    })


@app.route('/mixedquiz', methods=['POST'])
def update_quiz_results():
    data = request.data
    quiz_handler.update_quiz_results(data)
    return jsonify({
        'status': 'ok'
    })


if __name__ == '__main__':
    app.run()