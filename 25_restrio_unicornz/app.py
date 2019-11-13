# Manfred Tan, Brandon Chen
# SoftDev1 pd9
# k#25 - REST
# 2019-11-13

from flask import Flask, render_template
from urllib.request import urlopen, Request
import json
app = Flask(__name__) #create instance of class Flask

@app.route('/')
def home():
    return(render_template('home.html'))


@app.route("/trivia")
def trivia():
    link = urlopen("https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple")
    response = link.read()
    data = json.loads( response )

    results = data['results'][0] # enters into the list, which contains info
    question = results['question']
    correctAns = results['correct_answer']
    wrongAns = results['incorrect_answers'] # 0,1,2

    print(wrongAns[0])
    return(render_template('trivia.html',
        question = question,
        correctAns = correctAns,
        wrongAns = wrongAns))


@app.route("/nhl")
def nhl():
    link = urlopen('https://statsapi.web.nhl.com/api/v1/schedule')
    response = link.read()
    data = json.loads(response)

    allMatches = data['dates'][0]
    date = allMatches["date"]
    numOfGames = allMatches['totalGames']
    games = allMatches["games"]
    #game = games[0]
    #teams = game['teams']
    #homeTeam = game['teams']['home']['team']['name']
    #JINJA CODE IN HTML FILE:
    #game['teams']['home']['team']['name']}} vs {{game['teams']['away']['team']['name']}}, at {{game['venue']['name']}
    #print(homeTeam)
    return(render_template('nhl.html',
        date = date,
        numOfGames = numOfGames,
        games = games
        ))


if __name__ == "__main__":
    app.debug = True
    app.run()