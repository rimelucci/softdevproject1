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

    if 'n' not in session:
        session['n'] = False
    
    if util.authenticate(user,password):
        session['n'] = True
        return redirect(url_for("login", message = "you have successfully logged in"))
        
    return render_template("login", message = "incorrect username or password")
    

@app.route("/reset")
def reset():
    session['n'] = False
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
