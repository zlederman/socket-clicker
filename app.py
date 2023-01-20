from flask import Flask, send_from_directory, render_template
from flask_socketio import SocketIO, emit
from html.parser import HTMLParser
app = Flask(__name__,static_folder="public",template_folder="templates")
socketio = SocketIO(app)
counter = 0

@socketio.on('message')
def handle_message(data):
    print(f"recieved: {data}")

@socketio.on('increment')
def handle_increment():
    global counter
    counter += 1
    emit('updated-counter',counter,broadcast=True)

@app.route('/')
def send_index():
    global counter
    return render_template("index.html",count=counter)

@app.route('/<path:filename>')
def send_static(filename):
    print(filename)
    return send_from_directory(app.static_folder,filename)



if __name__ == "__main__":
    socketio.run(app)