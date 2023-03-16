from flask import Flask, redirect, url_for, render_template, request, send_file
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@db/flaskcodeloop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class messageInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    username = db.Column(db.String(100), unique = True)
    message = db.Column(db.String(100))
    
    def __init__(self, date_time, username, message):
        self.date_time = date_time
        self.username = username
        self.message = message

@app.route("/<room_id>")
def index(room_id):
    return render_template("index.html", room=room_id)

@app.route("/api/chat/<room_id>", methods=["GET", "POST"])
def chatroom(room_id):
    if request.method == "GET":
        return send_file(f"chats/chat_{room_id}.txt", mimetype='text/plain')
    else: # POST
        user_name = request.form["username"]
        message = request.form["msg"]
        date_time = get_datetime()
        add_message_to_txt_file(room_id, user_name, message, date_time)
        return redirect(url_for("chatroom"))
        
def get_datetime():
    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return date_string
    
def add_message_to_txt_file(room_id, user_name, message, date_time):
    with open(f"chats/chat_{room_id}.txt","a+") as f:
        f.write(f"[{date_time}] {user_name}: {message}\n")
        
def get_full_chat_messages(room_id):
    with open(f"chats/chat_{room_id}.txt") as f:
        lines = f.readlines()
        return lines
    
if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0")