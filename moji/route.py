from moji import app ##flaskを使ってユーザが作ったモジュールをインポートする
from flask import render_template,request, jsonify
from moji import socketio
import speech_recognition as sr
import requests

is_recording = False  # 録音状態

# メモページ
@app.route('/')
def memo_page():
    return render_template('memo.html')

# esa API設定
ESA_API_URL = "https://api.esa.io/v1/teams/tamadalab/posts"
ESA_ACCESS_TOKEN = "c7XECIvzw4aNy7WvFze4lldhSyRjjyVXrj83CLlrJPU"

@app.route('/save-to-esa', methods=['POST'])
def save_to_esa():
    data = request.json
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ESA_ACCESS_TOKEN}"
    }
    response = requests.post(ESA_API_URL, headers=headers, json=data)
    return jsonify(response.json()), response.status_code

# 音声認識処理
def recognize_audio():
    global is_recording
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            if is_recording:
                print("録音中...")
                try:
                    audio = recognizer.listen(source, timeout=5)
                    text = recognizer.recognize_google(audio, language="ja-JP")
                    print(f"認識結果: {text}")
                    socketio.emit('transcription', {'text': text})
                except sr.UnknownValueError:
                    socketio.emit('transcription', {'text': '（認識できませんでした）'})
                except sr.RequestError as e:
                    socketio.emit('transcription', {'text': f'エラー: {e}'})

# 録音制御用のSocket.IO
@socketio.on('start_recording')
def start_recording():
    global is_recording
    is_recording = True
    print("=== 録音を開始しました ===")

@socketio.on('stop_recording')
def stop_recording():
    global is_recording
    is_recording = False
    print("=== 録音を停止しました ===")
