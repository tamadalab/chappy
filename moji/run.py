from moji import app  # your_app_name はアプリケーションフォルダ名に置き換えてください
import threading
from moji import socketio
from moji.route import recognize_audio

if __name__ == '__main__':
    # 音声認識を別スレッドで実行
    threading.Thread(target=recognize_audio, daemon=True).start()
    # Flaskアプリを起動
    socketio.run(app, debug=True,host='127.0.0.1', port=5000)
