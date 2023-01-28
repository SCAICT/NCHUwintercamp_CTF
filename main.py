from flask import *
import time
import sqlite3
import os

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def login_page():
    files = ["cat-turtle.png",
"CLoveYC-turtle.png",
"earth-turtle.png",
"goast-turtle.png",
"laugh-turtle.png",
"melt-turtle.png",
"monkey-turtle.png",
"one-eyed-turtle.png",
"pig-turtle.png",
"rabbit-turtle.png",
"sad-turtle.png",
"skeleton-turtle.png",
"thumb-turtle.png",
"tiger-turtle.png",
"toast-turtle.png",
"virus-turtle.png"]
    dic = {}
    dicn = {}
    k = 1
    cookie = 0
    for file in files:
        dic[file] = k
        dicn[k] = file
        k += 1
    print(k)
    if request.method == 'POST':
        search_term = request.form["turtle"]
        search_term += ".png"
        html = render_template("login.html")
        for file in files:
            if search_term == file:
                results=file
                html = render_template("login.html",results = results)
                cookie = dic[file]
        resp = make_response(html)
        resp.set_cookie(key='turtle', value=str(cookie).encode(), expires=time.time()+6*60)
    else:
        try:
            if 'turtle' in request.cookies:
                turtle = int(request.cookies.get('turtle'))
            else:
                turtle = -1
        except:
            turtle = -1
        if turtle > 0 and turtle < k:
            results = dicn[turtle]
            html = render_template("login.html",results = results)
            cookie = turtle
        elif turtle == k:
            html = render_template("flag.html")
        else:
            html = render_template("login.html")
        resp = make_response(html)
        resp.set_cookie(key='turtle', value=str(cookie).encode(), expires=time.time()+6*60)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
