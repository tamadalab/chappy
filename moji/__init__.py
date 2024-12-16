from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memo_data.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db = SQLAlchemy(app)
socketio = SocketIO(app)

from moji.models import MemoData
with app.app_context():
    db.create_all()

from moji import route
