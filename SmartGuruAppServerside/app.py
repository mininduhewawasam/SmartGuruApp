from flask import Flask, jsonify, request, session

import videosuggestions
import stacklinkssuggestions
import recQuizGenerator
import randQuestions
import addQuestionsToDB
import viewUsers
import SessionHandler
import RegisterUsers
import analyze_performance as analyzer
import quiz_result_handler as quiz_handler
import lesson_quiz_generator
import leaderboard
import edit_profile as profile
import json


app = Flask(__name__)

@app.route('/youtubelinks')
def youtube():
    return videosuggestions.vediolinks()


@app.route('/stackoverflowlinks')
def stackoverflow():
    return stacklinkssuggestions.stacklinks()

@app.route('/leaderboardlist')
def leaderboardmarks():
  return leaderboard.sortedmarks()

@app.route('/recomand')
def recomendedQuiz():
    return recQuizGenerator.sendQuestions()


@app.route('/lessons/<string:level>/<string:lesson>')
def get_questions(lesson, level):
    return lesson_quiz_generator.get_questions(lesson, level)


@app.route('/performance/<int:user_id>', methods=['GET'])
def get_performance(user_id):
    return analyzer.calculate_performance(user_id)


@app.route('/random')
def randomQuiz():
    return randQuestions.generaterandmQuiz()

@app.route('/addQS')
def addQuestions():
    return addQuestionsToDB.addQuestions()

@app.route('/users')
def showUsers():
    return viewUsers.displayUsers()

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

@app.route('/register')
def register():
    return RegisterUsers.signUp()

@app.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    if request.method == "GET":
        return profile.get_user_details(session['user'])
    if request.method == "POST":
        data = request.data
        return profile.update_user_details(session['user'], data)

@app.route('/mixedquiz', methods=['POST'])
def update_quiz_results():
    data = request.data
    quiz_handler.update_quiz_results(data)
    return jsonify({
        'status': 'ok'
    })


if __name__ == '__main__':
    app.run()
