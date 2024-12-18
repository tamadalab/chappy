from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__,static_folder='icons')
socketio = SocketIO(app)

from moji import route
