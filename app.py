from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")















if __name__ == "__main__":
    app.debug = True
    app.secret_key="secret"
    app.run(host = "0.0.0.0", port = 8000)
