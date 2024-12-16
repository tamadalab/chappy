from moji import app ##flaskを使ってユーザが作ったモジュールをインポートする
from flask import render_template,redirect, url_for,flash,request,jsonify
from moji import db
from moji.models import MemoData,MojiData
import os
import openai
import tkinter as tk ##GUI構築のライブラリ
from tkinter import filedialog 
from flask_socketio import SocketIO
from moji import socketio
import speech_recognition as sr

is_recording = False

# メモのルート
@app.route('/')
@app.route('/memo',methods=['GET','POST'])
def memo_page():
    memodata = MemoData.query.all()
    mojidata = MojiData.query.all()
    return render_template('memo.html',memodata=memodata,mojidata=mojidata)


#メモ保存ルート
@app.route('/save-memo',methods=['POST','GET'])
def save_memo():
    memo = MemoData()
    data = request.get_json() ##送信されたJSON形式のデータを代入
    new_content = data.get('content')
    new_title = data.get('title')
    id = data.get('id')

    if  memo.id_check(id):
        existing_memo = MemoData.query.get(id)
        if existing_memo:
            # レコードを更新
            existing_memo.title = new_title
            existing_memo.content = new_content
            db.session.commit()
    else:
        new_memo = MemoData(content=new_content,title=new_title,)
        db.session.add(new_memo)
        db.session.commit()

    if not new_content:
        return jsonify({'error': '内容がないよう'}),400
    
    return jsonify({'message': '成功したよう'}),200

@app.route('/del-memo',methods=['POST','GET'])
def del_memo():
    memo = MemoData()
    data = request.get_json() ##送信されたJSON形式のデータを代入
    id = data.get('id')

    if  memo.id_check(id):
        existing_memo = MemoData.query.get(id) ##主キーをもとにデータベース代入
        db.session.delete(existing_memo)
        db.session.commit()
        return jsonify({'message': '成功したよう'}),200
    
    return jsonify({'error': '失敗した'}),401

@app.route('/save-moji',methods=['POST','GET'])
def save_moji():
    moji = MojiData()
    data = request.get_json() ##送信されたJSON形式のデータを代入
    new_content = data.get('content')
    new_title = data.get('title')
    id = data.get('id')

    if  moji.id_check(id):
        existing_memo = MojiData.query.get(id)
        if existing_memo:
            # レコードを更新
            existing_memo.title = new_title
            existing_memo.content = new_content
            db.session.commit()
    else:
        new_moji = MojiData(content=new_content,title=new_title,)
        db.session.add(new_moji)
        db.session.commit()

    if not new_content:
        return jsonify({'error': '内容がないよう'}),400
    
    return jsonify({'message': '成功したよう'}),200

@app.route('/del-moji',methods=['POST','GET'])
def del_moji():
    moji = MojiData()
    data = request.get_json() ##送信されたJSON形式のデータを代入
    id = data.get('id')

    if  moji.id_check(id):
        existing_moji = MojiData.query.get(id) ##主キーをもとにデータベース代入
        db.session.delete(existing_moji)
        db.session.commit()
        return jsonify({'message': '成功したよう'}),200
    
    return jsonify({'error': '失敗した'}),401
    

def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for note-taking."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error: {str(e)}"


def recognize_audio():
    global is_recording
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # ノイズ調整
        while True:
            if is_recording:
                print("Listening...")
                try:
                    audio = recognizer.listen(source, timeout=5)  # 音声取得
                    text = recognizer.recognize_google(audio, language="ja-JP")  # 日本語文字起こし
                    print(f"Recognized: {text}")
                    socketio.emit('transcription', {'text': text})  # Web画面に送信
                except sr.UnknownValueError:
                    socketio.emit('transcription', {'text': '（認識できませんでした）'})
                except sr.RequestError as e:
                    socketio.emit('transcription', {'text': f'エラー: {e}'})


def control_recording():
    global is_recording
    print("=== 録音開始と停止を制御します ===")
    print("Enterキーを押すと録音開始・停止を切り替えます")
    print("終了する場合はCtrl+Cを押してください\n")

    while True:
        input()  # Enterキー入力待機
        is_recording = not is_recording
        if is_recording:
            print("=== 録音を開始しました ===")
        else:
            print("=== 録音を停止しました ===")
