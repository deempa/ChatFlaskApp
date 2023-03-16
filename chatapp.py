from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/<room_id>")
def index(room_id):
    return render_template("index.html")

app.route("/chat/<room_id>", methods=["GET", "POST"])
def add_message(rood_id):
    if request.method == "GET":
        pass
    else: # POST
        user_name = request.form["username"]
        message = request.form["msg"]
        

def get_datetime():
    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return date_string
    

if __name__ == "__main__":
    app.run()