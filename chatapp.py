from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<room_id>")
def index(room_id):
    return render_template("index.html")

if __name__ == "__main__":
    app.run()