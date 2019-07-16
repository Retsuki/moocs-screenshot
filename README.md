# これはMoocs専用自動スクショコードです
## 手順
まず、以下のサイトからchromedriverを取得します
### http://chromedriver.chromium.org/downloads
自分と同じOSのdriverをダウンロードしてください。

* pyautoguiのパッケージが入っていない場合は以下実行

pip3 install pyautogui

auto.pyと同じディレクトリにchromedriverを起きましょう。

# 実行

python auto.py

1, INIADのメールやID, Passwordを自分のものに当ててください。

2, スクショしたいmoocsのURLを指定してください

3, スライドの枚数も指定してください。

### 注意事項
1, このプログラムはまだまだ改善するべきものがたくさんあるため、指定したURLのスライドのみのスクショになります。ご了承ください。

2, カーソルの位置などはもしかしたらPCによって若干の違いがございます。カーソルの位置取得コードを置いておきました。
