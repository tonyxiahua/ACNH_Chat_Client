# 动森说话机（原本ACNH_Chat_Client）
## 介绍
这是一个Fork之后被我魔改的项目
通过Nintendo Switch Online 进行聊天的简化版，再也不用拿着手机和人对话了，也可以用机器自动发送一些消息
暂时是开源项目。还需要很长的代码优化。

Update History:
2021-6-18 重写README.md
2021-6-17 First Commit 改变语言为中文的选项。并且修正了不能连接的版本号码。

Special thanks for collecting this all together

## 改変について
[acnh_chat_gui.py](acnh_chat_gui.py)はMIT Licenseです。自由に改変して使っていただいて構いません。
私自身、GUIの見た目やプログラムの改善点など沢山あると思っているのでプルリク大歓迎です。
[acnh_info_edited.py](acnh_info_edited.py)はxSke氏が書いた物が元なので何とも言えません...
もし、このプログラムが消えてたら察してください😇

## 使用说明
1. 安装所需程序包 运行 
```
pip install -r requirements.txt
```

2. 安装完成后运行
```
python acnh_info_edited.py
```
3. Nintendo Switch Online 将会要求你登陆，自动跳转到登陆的界面，然后输入信息之后登陆。
4. 本次过程不会收集你的任何信息，所有步骤都在你本地的电脑完成。 右键复制红色登陆的连接
5. 之后将信息复制黏贴到本程序里面进行分析
6. 制作你本次的ACNH Token
7. 最后运行acnh_chat_gui.py 或者 acnh_reaction_gui.py （好友的User ID等信息 可以选择填写）
8. 输入你的ACNH Token 就可以发送信息了。


## Special Thanks
[ mizuyoukanao/ACNH_Chat_Client](https://github.com/mizuyoukanao/ACNH_Chat_Client)
[dqn's blog](https://dqnn.hatenablog.com/entry/2020/05/02/005843)、およびに[githubリポジトリ](https://github.com/dqn/acnh)、
[こちらのissuesも参考になりました。](https://github.com/ZekeSnider/NintendoSwitchRESTAPI/issues/13)改めて感謝します!
