import itchat
import copy
from itchat.content import *
from docx import Document
from docx.shared import Inches

@itchat.msg_register(TEXT, isGroupChat=True)
def store_msg(msg):
    path = "rixinbiji/"
    lev = 1
    # 找到对应群
    # 获取群成员姓名ID信息对照表
    # 接收信息存储word文档
    document = Document()
    if msg["ToUserName"] == "@@e28f83b78e243e90d50a149d0d1abc6ad3d9782be2dd6c89acecfd8ab7e7e57d":
        if "日新笔记" in msg["Content"]:
            # content = fileterEmoji(msg["Content"])
            content = copy.deepcopy(msg["Content"])
            text = content.split('\n')
            document.add_heading(text[0], level=lev)
            for txt in text[1:]:
                document.add_paragraph(txt)
            document.add_paragraph('\n')

def fileterEmoji(contents):
    content = copy.deepcopy(contents)
    for i, chr in enumerate(content):
        if chr in range(0x1f600, 0x1f650):
            contents[i] == ' '
    return content

if __name__ == "__main__":
    groupName = "北十七青年营"
    keyWord = "日新笔记"
    # 登录
    itchat.auto_login(hotReload=True)
    # 接收消息
    # 判断是否来自希望的群聊
    # 如果是来自于希望的群聊
        # 判断发送的消息中是否含有希望的关键字
            # 如果包含希望的关键字
                # 判断文件夹内
            # 如果不包含希望的关键字：重新监控消息
    # 如果不是来自于希望的群聊
    document = Document()
    document.add_heading()

    houchu = itchat.search_chatrooms(userName="北十七志愿者")



