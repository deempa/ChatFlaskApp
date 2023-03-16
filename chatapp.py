from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/<room_id>")
def index(room_id):
    return render_template("index.html")

app.route("/chat/<room_id>", methods=["GET", "POST"])
def add_message(room_id):
    if request.method == "GET":
        pass
    else: # POST
        user_name = request.form["username"]
        message = request.form["msg"]
        date_time = get_datetime()
        add_message_to_txt_file(room_id, user_name, message, datetime)
        
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
    app.run()