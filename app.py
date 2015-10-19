from flask import Flask, render_template, session, redirect, url_for, request, flash, Markup
import util

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", session=session)

@app.route("/about")
def about():
    return render_template("about.html", session=session)

@app.route("/story")
def story():
#generates html for displaying the title as a link
    str=""
    stories=util.getAllPosts()
    if not stories:
        str+='<br><br>'
        str+='"<div class="col-md-offset-2 col-md-8 row">'
        str+='<h2 class="text-primary text-center"> %s </h2>' %("Add a story above!")
        str+='</div>'
    for item in reversed(stories):
        str+='"<div class="col-md-offset-2 col-md-8 row" style="background-color:black; opacity:0.8">'
        str+='<h2 class="text-primary" style="word-wrap: break-word"> %s </h2>' %(item[1])
        str+="<blockquote>"
        str+='<p class="text-warning" style="word-wrap: break-word">%s</p>' %(item[2])
        str+='<footer class="text-info">%s</footer>' %(item[0])
        str+="</blockquote>"
        str+="</div>"

    str = Markup(str)

    return render_template("story.html", allposts=str)
   # return render_template("story.html")

@app.route("/login", methods = ["GET"])
def login():
    if 'username' in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def login2():
    user = request.form['username']
    password = request.form['password']
    button = request.form['button']

    if util.authenticate(user,password):
        session['username'] = user
        flash("You were successfully logged in")
        return redirect(url_for("home"))
    flash("Invalid Username or Password")
    return render_template("login.html", session=session)
    

@app.route("/newpost", methods=['GET','POST'])
def newpost():
    if request.method=="GET":
        return render_template("newpost.html")
    else:
        uname=session['username']
        button=request.form['button']
        title=request.form['nTitle']
        content=request.form['nContent']
        if button=="Post":
            util.makePost(uname,title,content)
            return redirect(url_for('story'))
        if button=="cancel":
            return redirect(url_for('home'))
        return render_template('newpost.html', session=session)


@app.route("/reset")
@app.route("/logout")
def reset():
    #works whether or not 'username' is in session
    session.pop('username', None);
    return redirect(url_for("home"))

@app.route("/register", methods=['GET','POST'])
def register():
	if request.method=="GET":
		return render_template("register.html")
        else:
            username = request.form['username']
            password = request.form['password']
            if util.registerCheck(username):
                util.register(username,password)
                return redirect(url_for("login"))
            else:
                flash("Please choose a different Username")
                return redirect(url_for("register"))

if __name__ == "__main__":

    util.initializeTables()
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
