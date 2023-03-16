from flask import Flask, redirect, url_for, render_template, request, send_file
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import socket

db = SQLAlchemy()
     
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@db:3306/chatapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db.init_app(app)

class messageInfo(db.Model):
    id = db.Column("id" ,db.Integer, primary_key = True)
    chat_id = db.Column("chat_id", db.Integer)
    date_time = db.Column("date_time", db.String(100))
    username = db.Column("username" ,db.String(100))
    message = db.Column("message", db.String(100))
    
    def __init__(self, chat_id, date_time, username, message):
        self.chat_id = chat_id
        self.date_time = date_time
        self.username = username
        self.message = message
        
    def __str__(self) -> str:
        return f"{self.date_time} | {self.username}: {self.message}\n"

@app.route("/<room_id>")
def index(room_id):
    return render_template("index.html", room=room_id)

@app.route("/api/chat/<room_id>", methods=["GET", "POST"])
def chatroom(room_id):
    if request.method == "GET":
        messages = get_full_chat_messages(room_id)
        return messages, 200, {'Content-Type': 'text/plain'}

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
    new_message = messageInfo(room_id, date_time, user_name, message)
    db.session.add(new_message)
    db.session.commit()
    
def get_full_chat_messages(room_id):
    messages = db.session.query(messageInfo).filter(messageInfo.chat_id == room_id)
    fulltext = ""
    for msg in messages:
        fulltext += str(msg)
    return fulltext
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0")