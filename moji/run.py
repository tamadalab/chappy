from moji import app  # your_app_name はアプリケーションフォルダ名に置き換えてください
import threading
from flask_socketio import SocketIO
from moji import socketio
import speech_recognition as sr
from moji.route import recognize_audio,control_recording

if __name__ == '__main__':
    # 音声認識を別スレッドで実行
    threading.Thread(target=recognize_audio, daemon=True).start()
    # 録音制御スレッド
    threading.Thread(target=control_recording, daemon=True).start()
    # Flaskアプリを起動
    socketio.run(app, debug=True)
