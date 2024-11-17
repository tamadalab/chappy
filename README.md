# モジッピー
### 概要
このプロジェクトは、音声認識技術を活用して音声データを自動的に文字起こしを行い、Webアプリ上で結果を表示するツールです。会議録の作成や講義の記録など、効率的な文字起こしをサポートします。

### 主な機能
・リアルタイム音声認識： 録音中の音声を即座に文字起こし

### 使用方法　
・インストール手順

・ツールの使い方
### 開発環境
#### 使用技術とライブラリ
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fimg.shields.io%2Fbadge%2F-Python-F2C63C.svg%3Flogo%3Dpython%26style%3Dfor-the-badge?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c17144ccc12f9c19e9dbba2eec5c7980"> <img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fimg.shields.io%2Fbadge%2F-JavaScript-000000.svg%3Fstyle%3Dfor-the-badge%26logo%3DJavaScript%26logoColor%3DF7DF1E?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7a90e0e66d0f873de7b7fe04977968ba"><img src="https://img.shields.io/badge/-Vue.js-4FC08D.svg?logo=FFLASK&style=plastic">

| 種類              | 技術・ライブラリ      | バージョン  | 説明                                    |
|-------------------|-----------------------|------------|---------------------------------------|
| プログラミング言語 | Python               | 3.9以上     | プロジェクト全体で使用する主要な言語     |
| フレームワーク     | Flask                | 2.1.3      | Webアプリケーションフレームワーク  |
| リアルタイム通信   | Flask-SocketIO       | 5.3.1      | WebSocket通信をサポートするライブラリ   |
| 音声処理           | PyAudio              | 0.2.11     | マイクから音声をキャプチャするライブラリ |
| 音声認識エンジン   | Vosk                 | 0.3.45     | オフライン音声認識を可能にするエンジン   |
| テンプレートエンジン | Jinja2               | Flask組み込み| HTMLテンプレートを生成するエンジン       |
#### 必要なツールのインストール方法
・Pythonのインストール

Python 3.9以上を以下のURLからインストールしてください

https://www.python.org

・ライブラリのインストール

以下のコマンドでインストールするか、requirements.txt に記載してください。

```pip install flask flask-socketio pyaudio vosk```

・音声認識モデル

Voskの日本語モデル: vosk-model-small-ja-0.22

モデルファイルはVosk公式サイト(https://alphacephei.com/vosk/models) からダウンロードし、プロジェクトのディレクトリに配置してください
#### ローカルでの実行方法

以下のコマンドで起動する

```python app.py```

ローカルサーバーにアクセスする。デフォルトは以下のURLである

```http://127.0.0.1:5000```


