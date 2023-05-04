import os
import PySimpleGUIQt as sg
from PIL import Image, ImageSequence

# GUIのレイアウト
layout = [
    # 上部のフレーム
    [sg.Frame(title="ファイルパスを入力してください",
        layout=[
            [sg.Multiline(key="-file_path-", enable_events=True),
            sg.FileBrowse("開く", key="-browse-")],
            [sg.Text("保存場所を選択"),
            sg.Input(key="-save_path-"),
            sg.FolderBrowse("開く", key="-folder_browse-")]
        ])],
    # 下部のフレーム
    [sg.Frame(title="",
              layout=[
                  [sg.Button("抽出", key="-extract-")]
              ])]
]
# ウィンドウを作成
window = sg.Window("Image Converter", layout, size=(500, 200))

# イベントループ
while True:
    event, values = window.read()  # イベントを取得

    # ウィンドウを閉じたら終了
    if event == sg.WINDOW_CLOSED:
        break

    # ファイルを選択したら、テキストボックスにパスを表示
    if event == "-browse-":
        window["-file_path-"].update(value=values["-browse-"])

    # 抽出ボタンが押されたら
    if event == "-extract-":
        # ファイルパスを取得
        file_path = values["-file_path-"]
        # 改行でファイルパスを分けてリストで格納
        file_path = file_path.splitlines()
        

# ウィンドウを閉じる
window.close()