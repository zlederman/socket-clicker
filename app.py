from flask import Flask, send_from_directory, render_template, request
from flask_socketio import SocketIO, emit, join_room, send
from html.parser import HTMLParser
import rooms
import json

app = Flask(__name__,static_folder="public",template_folder="templates")
socketio = SocketIO(app)
room = rooms.Rooms()

@socketio.on('message')
def handle_message(data):
    print(f"recieved: {data}")

@socketio.on('increment')
def handle_increment(data):
    global room
    room_id = data["room"]
    count = room.increment_room_count(room_id)
    emit('updated-counter',count,broadcast=True)
    
@socketio.on('join')
def handle_join(data):
    global room
    uname = data['uname']
    room_id = room.add_user(uname,request)
    room_count = room.get_room_count(room_id)
    emit('join-res',{"uname":uname, "room":str(room_id),"count":room_count})

@app.route('/')
def send_index():
    return send_from_directory(app.static_folder,"index.html")

@app.route('/clicker',methods=["GET"])
def send_clicker():
    return render_template("clicker.html",count="Loading...",room_id="Loading...",username="Loading...")


@app.route('/<path:filename>')
def send_static(filename):
    print(filename)
    return send_from_directory(app.static_folder,filename)



if __name__ == "__main__":
    socketio.run(app)