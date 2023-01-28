from flask import *
import time
import sqlite3
import os

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def login_page():
    html = render_template("login.html")
    resp = make_response(html)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
