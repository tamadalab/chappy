# モジッピー
### 概要
このプロジェクトは、音声認識技術を活用して音声データを自動的に文字起こしを行い、Webアプリ上で結果を表示するツールです。会議録の作成や講義の記録など、効率的な文字起こしをサポートします。

### 主な機能
・リアルタイム音声認識： 録音中の音声を即座に文字起こし

### 使用方法　
・インストール手順

・ツールの使い方
### 開発環境
##### 使用技術とライブラリ
・フレームワーク: Flask

・リアルタイム通信: Flask-SocketIO

・PyAudio: マイク入力を処理

・Vosk: 音声認識エンジン

・データフォーマット: JSON
##### ライブラリのダウンロード方法

以下のコマンドでインストールするか、requirements.txt に記載してください。

```pip install flask flask-socketio pyaudio vosk```
##### 音声認識モデル
・Voskの日本語モデル: vosk-model-small-ja-0.22

モデルファイルはVosk公式サイト(https://alphacephei.com/vosk/models) からダウンロードし、適切なパスに配置してください。
### 開発者
