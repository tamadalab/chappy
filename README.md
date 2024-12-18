
# モジッピー
<img width="464" alt="スクリーンショット 2024-11-11 10 47 16" src="https://github.com/user-attachments/assets/fb95e6f0-34c3-4ded-9a3c-14a66b9a092e">

### 概要
音声認識技術を活用して音声データを自動的に文字起こしを行い、Webアプリ上で結果を表示するツールです。会議録の作成や講義の記録など、効率的な文字起こしをサポートする。

### 主な機能
・リアルタイム音声認識： 録音中の音声を即座に文字起こし

・メモ：メモを残せる

・esaと共有：内容をesaと共有できる

### 使用方法　
・インストール手順

・ツールの使い方
### 開発環境
#### 使用技術とライブラリ
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fimg.shields.io%2Fbadge%2F-Python-F2C63C.svg%3Flogo%3Dpython%26style%3Dfor-the-badge?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c17144ccc12f9c19e9dbba2eec5c7980"> <img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fimg.shields.io%2Fbadge%2F-JavaScript-000000.svg%3Fstyle%3Dfor-the-badge%26logo%3DJavaScript%26logoColor%3DF7DF1E?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7a90e0e66d0f873de7b7fe04977968ba">
| 種類              | 技術・ライブラリ      | バージョン  | 説明                                    |
|-------------------|-----------------------|------------|---------------------------------------|
| プログラミング言語 | Python               | 3.9以上     | プロジェクト全体で使用する主要な言語     |
| フロントエンド     | JavaScript           | ES6以上     | Webアプリケーションの動的部分を担当     |
| フレームワーク     | Flask                | 2.1.3      | Webアプリケーションフレームワーク  |
| リアルタイム通信   | Flask-SocketIO       | 5.3.1      | WebSocket通信をサポートするライブラリ   |
| 音声処理           | speech_recognition            |  3.10.0      | マイクから音声をキャプチャするライブラリ |

#### 必要なツールのインストール方法
・Pythonのインストール

Python 3.9以上を以下のURLからインストールしてください

https://www.python.org

・ライブラリのインストール

以下のコマンドでインストールするか、requirements.txt に記載してください。

```pip install flask flask-socketio pyaudio  speech_recognition```

・音声認識モデル

#### ローカルでの実行方法

以下のコマンドで起動する

```python run.py```

ローカルサーバーにアクセスする。デフォルトは以下のURLである

```http://127.0.0.1:5000```


