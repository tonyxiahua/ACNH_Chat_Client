import tkinter
from tkinter import messagebox
from tkinter import ttk
import requests
import json
TK_SILENCE_DEPRECATION=1

url = "https://web.sd.lp1.acbaa.srv.nintendo.net/api/sd/v1/messages"

def button_click():
    if v.get() == '当地的':
        headers = {'Authorization': 'Bearer {}'.format(input_token.get())}
        payload = {"body": "{}".format(input_message.get()), "type": "keyboard"}
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        if r.status_code != 201:
            print("{}发生了错误".format(r.status_code))
        else:
            print("发送成功")
    if v.get() == '指定朋友':
        headers = {'Authorization': 'Bearer {}'.format(input_token.get())}
        payload = {"body": "{}".format(input_message.get()), "type": "friend", "userId": "{}".format(input_friendid.get())}
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        if r.status_code != 201:
            print("{}发生了错误".format(r.status_code))
        else:
            print("发送成功")
    if v.get() == '所有朋友':
        headers = {'Authorization': 'Bearer {}'.format(input_token.get())}
        payload = {"body": "{}".format(input_message.get()), "type": "all_friend"}
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        if r.status_code != 201:
            print("{}发生了错误".format(r.status_code))
        else:
            print("发送成功")

root = tkinter.Tk()
root.title("ACNH chat test")
root.geometry("500x120")

# メッセージラベル
input_message_label = tkinter.Label(text="消息（最多 32 个字符）")
input_message_label.grid(row=1, column=1)

# メッセージ入力欄
input_message = tkinter.Entry(width=32)
input_message.grid(row=1, column=2)

# TOKENラベル
input_token_label = tkinter.Label(text="ACNH TOKEN(请输入工具获取的token)")
input_token_label.grid(row=2, column=1)

# TOKEN入力欄
input_token = tkinter.Entry(width=32)
input_token.grid(row=2, column=2)

# 送信先ラベル
input_sendat_label = tkinter.Label(text="请选择目的地")
input_sendat_label.grid(row=3, column=1)

# 送信先選択欄
sendat = ['当地的', '指定的朋友', '所有朋友']
v = tkinter.StringVar()
input_sendat_cb = ttk.Combobox(textvariable=v, values=sendat, width=10)
input_sendat_cb.grid(row=3, column=2)

# フレンドのユーザーIDラベル
input_friendid_label = tkinter.Label(text="好友的用户ID（仅当目的地为“指定好友”时）")
input_friendid_label.grid(row=4, column=1)

# TOKEN入力欄
input_friendid = tkinter.Entry(width=18)
input_friendid.grid(row=4, column=2)

button = tkinter.Button(text="发送",command=button_click)
button.place(x=285, y=85, width=200)

root.mainloop()