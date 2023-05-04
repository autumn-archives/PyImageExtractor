import os
import PySimpleGUIQt as sg
from PIL import Image, ImageSequence

class ImageManager:
    """画像を操作するクラス"""
    #　コンストラクタ　初期値を""に設定
    def __init__(self,file_path="",save_path=""):
        self.file_path = file_path
        self.save_path = save_path
        
    """アニメーションgifやpngなどからイメージを抽出する処理"""
    def image_extractor(self,files,save_path):
            # 与えられたファイルリストから１つずつ処理
            for file_p in files:
                # D&Dした時などに勝手についてしまうfile:///を外す。
                file_p = file_p.removeprefix(r"file:///")
                # アニメーションを開く
                with Image.open(file_p) as im:
                    # アニメーションか判定
                    if im.is_animated == True:
                        #　アニメーションのファイル名、拡張子取得
                        file_p,ext = os.path.splitext(os.path.basename(file_p))
                        # カウンタを１にセット。１から開始
                        count = 1
                        # フレームごとに取り出す処理
                        for frame in ImageSequence.Iterator(im):
                            # 数字の０埋め処理
                            cnt_fill = str(count).zfill(2)
                            # フレームにファイル名と_XXと拡張子をくっつけて保存
                            frame.save(os.path.abspath(os.path.join(save_path,f"{file_p}""_"f"{cnt_fill}"f"{ext}")))
                            # カウントを増やす
                            count += 1
                        # 終わったらアニメーションごとに通知する
                        sg.popup(f"{file_p} から抽出し、{save_path} に保存しました。")
                    else:
                        # 失敗しても通知
                        sg.popup(f"{file_p} から抽出に失敗しました。アニメーションgif、png、webpかファイルが壊れていないか確認してください。")

def main():
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

if __name__ == "__main__":
    # イメージ処理用のクラスをインスタンス化
    image_manager = ImageManager()
    main()