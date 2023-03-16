from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<room_id>")
def home(room_id):
    return f"Youre in room {room_id}"

if __name__ == "__main__":
    app.run()