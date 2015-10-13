from flask import Flask, render_template, session, redirect, url_for, request
import util

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods = ["GET"])
def login():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def login2():
    user = request.form['username']
    password = request.form['password']
    button = request.form['button']

    if util.authenticate(user,password):
        if user not in session:
            session[user] = True
            
   # else:
   #     if user not in session:
   #         session[user] = False
   #         error = "invalid username or password"

#add an Error message to the login page when it's incorrect

    return redirect(url_for("home"))

#for basic purposes, user = "admin" and password = "password"

@app.route("/reset")
def reset():
    session['user'] = False
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
