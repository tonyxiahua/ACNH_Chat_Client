import tkinter
from tkinter import messagebox
from tkinter import ttk
import requests
import json

url = "https://web.sd.lp1.acbaa.srv.nintendo.net/api/sd/v1/messages"

def send(reaction):
    headers = {'Authorization': 'Bearer {}'.format(input_token.get())}
    payload = {"body": reaction, "type": "emoticon"}
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    if r.status_code != 201:
        print("{}エラーが発生しました。".format(r.status_code))
    else:
        print("送信に成功しました。")

def button_click():
    if v.get() == 'やぁ！':
        send("Greeting")
    elif v.get() == 'うんうん':
        send("Nodding")
    elif v.get() == 'イヤイヤ':
        send("Negative")
    elif v.get() == 'ねっ':
        send("Hello")
    elif v.get() == 'ニコニコ':
        send("Smiling")
    elif v.get() == 'ハッピー':
        send("HappyFlower")
    elif v.get() == 'ウキウキ':
        send("HappyDance")
    elif v.get() == 'わらう':
        send("Laughing")
    elif v.get() == 'まかせて！':
        send("Assent")
    elif v.get() == 'シャキーン':
        send("Shaki")
    elif v.get() == 'クルリンパ':
        send("Dance")
    elif v.get() == 'ガンバレー！':
        send("Cheering")
    elif v.get() == 'パチパチ':
        send("Clapping")
    elif v.get() == 'ペコリ':
        send("Apologize")
    elif v.get() == 'えっ？':
        send("Pardon")
    elif v.get() == 'はて？':
        send("QuestionMark")
    elif v.get() == 'あっ！':
        send("Aha")
    elif v.get() == 'ハッ！':
        send("Shocked")
    elif v.get() == 'ガーン！':
        send("Surprised")
    elif v.get() == 'しまった！':
        send("Oops")
    elif v.get() == 'テレる':
        send("Blushing")
    elif v.get() == 'もじもじ':
        send("Hesitate")
    elif v.get() == 'にがわらい':
        send("WrySmile")
    elif v.get() == 'ニヤリ':
        send("Grin")
    elif v.get() == 'ヤレヤレ':
        send("OhGeez")
    elif v.get() == 'うーん':
        send("Thinking")
    elif v.get() == 'あくび':
        send("Sleepy")
    elif v.get() == 'すやすや':
        send("Sleep")
    elif v.get() == 'こまる':
        send("Worried")
    elif v.get() == 'ためいき':
        send("Sighing")
    elif v.get() == 'がっくり':
        send("SadSpiral")
    elif v.get() == 'しつれん':
        send("BrokenHeart")
    elif v.get() == 'わーん':
        send("Crying")
    elif v.get() == 'ジロッ':
        send("Silent")
    elif v.get() == 'ムカッ':
        send("Outraged")
    elif v.get() == 'ヒュー':
        send("ColdChill")
    elif v.get() == 'あせる':
        send("Frantic")
    elif v.get() == 'ブルブル':
        send("Shaking")
    elif v.get() == 'くしゃみ':
        send("Sneezing")

root = tkinter.Tk()
root.title("ACNH reaction test")
root.geometry("500x80")

# TOKENラベル
input_token_label = tkinter.Label(text="ACNH TOKEN(ツールで取得したトークンを入力してください)")
input_token_label.grid(row=2, column=1)

# TOKEN入力欄
input_token = tkinter.Entry(width=32)
input_token.grid(row=2, column=2)

# 送信先ラベル
input_sendat_label = tkinter.Label(text="送信するリアクションを選んでください")
input_sendat_label.grid(row=3, column=1)

# 送信先選択欄
sendat = ['やぁ！', 'うんうん', 'イヤイヤ', 'ねっ', 'ニコニコ', 'ハッピー', 'ウキウキ', 'わらう', 'まかせて！', 'シャキーン', 'クルリンパ', 'ガンバレー！', 'パチパチ', 'ペコリ', 'えっ？', 'はて？', 'あっ！', 'ハッ！', 'ガーン！', 'しまった！', 'テレる', 'もじもじ', 'にがわらい', 'ニヤリ', 'ヤレヤレ', 'うーん', 'あくび', 'すやすや', 'こまる', 'ためいき', 'がっくり', 'しつれん', 'わーん', 'ジロッ', 'ムカッ', 'ヒュー', 'あせる', 'ブルブル', 'くしゃみ']
v = tkinter.StringVar()
input_sendat_cb = ttk.Combobox(textvariable=v, values=sendat, width=10)
input_sendat_cb.grid(row=3, column=2)

button = tkinter.Button(text="送信",command=button_click)
button.place(x=285, y=50, width=200)

root.mainloop()


'''

def button_click():
    if v.get() == '打招呼':
        send("Greeting")
    elif v.get() == '点头':
        send("Nodding")
    elif v.get() == '不是':
        send("Negative")
    elif v.get() == '你好':
        send("Hello")
    elif v.get() == '微笑':
        send("Smiling")
    elif v.get() == '开心':
        send("HappyFlower")
    elif v.get() == '开心跳舞':
        send("HappyDance")
    elif v.get() == '大笑':
        send("Laughing")
    elif v.get() == '同意':
        send("Assent")
    elif v.get() == '怀疑':
        send("Shaki")
    elif v.get() == '跳舞':
        send("Dance")
    elif v.get() == '庆祝':
        send("Cheering")
    elif v.get() == '拍掌':
        send("Clapping")
    elif v.get() == '抱歉':
        send("Apologize")
    elif v.get() == '再说一次':
        send("Pardon")
    elif v.get() == '问号':
        send("QuestionMark")
    elif v.get() == '感叹号':
        send("Aha")
    elif v.get() == '震惊':
        send("Shocked")
    elif v.get() == '惊讶':
        send("Surprised")
    elif v.get() == '哦靠':
        send("Oops")
    elif v.get() == '脸红':
        send("Blushing")
    elif v.get() == '犹豫':
        send("Hesitate")
    elif v.get() == '苦笑':
        send("WrySmile")
    elif v.get() == '奸笑':
        send("Grin")
    elif v.get() == '我的天':
        send("OhGeez")
    elif v.get() == '思考':
        send("Thinking")
    elif v.get() == '打瞌睡':
        send("Sleepy")
    elif v.get() == '睡觉':
        send("Sleep")
    elif v.get() == '担心':
        send("Worried")
    elif v.get() == '叹气':
        send("Sighing")
    elif v.get() == '悲伤':
        send("SadSpiral")
    elif v.get() == '伤心':
        send("BrokenHeart")
    elif v.get() == '哭泣':
        send("Crying")
    elif v.get() == '安静':
        send("Silent")
    elif v.get() == '愤怒':
        send("Outraged")
    elif v.get() == '冷颤':
        send("ColdChill")
    elif v.get() == '发疯':
        send("Frantic")
    elif v.get() == '抖动':
        send("Shaking")
    elif v.get() == '喷嚏':
        send("Sneezing")
'''