from businessView.page_个人中心 import page_个人中心
from common.loc import *


class page_登录12306(page_个人中心):



    parent=loc_class("android.webkit.WebView")
    child=loc_text("登陆12306")
    btn_登录12306=loc_child_ele(parent,child)


    def get_登录12306按钮(self):
        return self.get_元素文本(self.btn_登录12306,"btn_登录12306")



