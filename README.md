# Gyazo Uploader
Gyazoに画像をアップロードし、その画像URLを受け取るプログラムです。
いつかの勉強会用に作りました。


## 事前準備

### 1. Gyazoのアカウントを登録しておく
[https://gyazo.com/](https://gyazo.com/)

プログラミング以外にも、画像を簡単に共有できる面で登録しておくべきです。
アプリをインストールしてからでないとアカウント登録できないので、サイトの指示に従ってアカウントを登録してください。

### 2. Gyazo API にアクセスする
[https://gyazo.com/api](https://gyazo.com/api)

ここからAPIを利用するためのアクセストークンを入手しましょう。

``アプリケーションを登録`` をクリック
![https://i.gyazo.com/8351495277445d28732a33dbed9ed5e1.png](https://i.gyazo.com/8351495277445d28732a33dbed9ed5e1.png)

``Name`` にはわかりやすいアプリ名を、``Callback URL``はなんでもいいですが、迷うなら ``http://example.com/`` と入れておきましょう。

``Submit`` を押してアプリを登録しましょう。
![https://i.gyazo.com/096b1cd5bf7f6c5d38cb73051f829166.png](https://i.gyazo.com/096b1cd5bf7f6c5d38cb73051f829166.png)

先ほど作ったアプリのアプリ名をクリックしましょう。
![https://i.gyazo.com/fb3fafe28943d0a177ad15f393c21faa.png](https://i.gyazo.com/fb3fafe28943d0a177ad15f393c21faa.png)

``Your access token`` の ``Generate`` をクリックしてアクセストークンを生成しましょう。

そこで生成されたトークンをコピーしておきましょう。
![https://i.gyazo.com/7d2dc7df9f8cbdd192097617d10b0f1c.png](https://i.gyazo.com/7d2dc7df9f8cbdd192097617d10b0f1c.png)

### 3. ライブラリをインストール
お使いのPCに以下のコマンドを実行して、python-gyazoをインストールする
```Shell
pip install python-gyazo
```

Herokuで使用する場合は、以下を``requirements.txt``に書き足す
```Plain Text
python-gyazo==2.0.0
```

### 4. コードをいじろう
7行目のXXXとなっている部分に、先ほどコピーしたアクセストークンを入れましょう。

これでとりあえず使用できるようになりました。後はアップロードするファイルを変えたり、他のプログラムに組み込んで使用してみてください。