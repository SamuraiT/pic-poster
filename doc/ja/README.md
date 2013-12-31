概要
----
写真を写して，それをtweetするtweeter botです．
このbotは基本的にイベントで使われるのを想定されています．
そのためローカルLan内では，誰でもアクセスでき，誰でも写真を
撮影できtweeterに投稿することができます．

使い方
------
まず`pic-poster`ディレクトリへ移動してください．
次に，`python manage.py`コマンドをterminalで叩くと：

```python
* Running on http://0.0.0.0:5000/
* Restarting with reloader
```
が表示されます．
ブラウザを開き，`http://raspberyのipアドレス:5000/`を叩いてください．
そうすると:
![index]('../img/index.png')
が表示されるので，comment欄にコメントを書き
hashtag欄にハッシュタグを書き込んで下さい．デフォルトでは
`#asahikawa_python`がハッシュタグとなります．

開発者へ
-------
このアプリケーションを動かさす上で必要となる
サードパーティモジュールのインストールは以下のコマンドで可能である．

```pip install -r requirements-flask.txt```
```pip install -r requirements-picbot.txt```

`-flask`でwebアプリケーションに必要なライブラリを
`-picbot`で写真をとるためのライブラリとtweetするための
ライブラリをインストールする事が出来ます．

**注意**
`picbot`ディレクトリにある`settings-sample.py`を
`settings.py`に変え，アクセスキーなど必要となる情報を
入力の上，運用してください．
また，デフォルトのハッシュタグである`HASH_TAG`を変更し，
`templates`にある，`index.html`の`hashtag`プレスホルダー
の値を変えてください

**動作環境**
動作保証している環境は
Debian/ubuntu下のみです．


ライセンス
-------
英語のドキュメントを参照してください．
