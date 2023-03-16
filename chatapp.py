from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/<room_id>")
def index(room_id):
    return render_template("index.html")

app.route("/chat/<room_id>", methods=["GET", "POST"])
def add_message(rood_id):
    if request.method == "GET":
        pass
    else: # POST
        pass
    

if __name__ == "__main__":
    app.run()