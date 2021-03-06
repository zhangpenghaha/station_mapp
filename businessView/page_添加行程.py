from appium.webdriver.common.touch_action import TouchAction

from common.loc import *
from businessView.page_行程 import page_行程


class page_添加行程(page_行程):
    "定位器!!!!!!!!!!!!!!!!!!!!!!!"

    btn_添加行程_车次查询 = loc_text("车次添加")

    btn_车次号输入框 = loc_text("例如：G9")

    btn_添加行程_站站查询 = loc_text("站站添加")

    btn_添加行程_出发地 = loc_text("出发地")

    btn_添加行程_目的地 = loc_text("目的地")

    btn_今天 = loc_text("今天")

    btn_添加行程_查询 = loc_text("查询")

    ipt_添加行程_车次号输入框=loc_id("ATadd1")

    "操作层"
    def get_行程信息(self, text):
        return self.find_loc_with_scroll(text)

    def send_输入车次(self, text):
        self.click_点击(self.btn_车次号输入框, "点击车次号输入框")
        return self.act_键盘输入(text)

    def get_起始站信息(self, text):
        text_起始站 = loc_text(text)
        self.get_元素文本(text_起始站, "获取起始站信息")

    def get_添加行程_站站查询(self):
        a=self.get_元素文本(self.btn_添加行程_站站查询, "btn_站站查询")
        return judgement(a,"站站添加")

    def get_添加行程_车次查询(self):
        a = self.get_元素文本(self.btn_添加行程_车次查询, "btn_车次查询")
        return judgement(a, "车次查询")

    def click_添加行程_查询(self):
        return self.click_点击(self.btn_添加行程_查询,"btn_添加行程_查询")

    def click_添加行程_查询方式(self, text):
        btn_添加行程_查询方式 = loc_text(text)
        return self.click_点击(btn_添加行程_查询方式,"btn_添加行程" + btn_添加行程_查询方式)

    def click_添加行程_车次查询(self):
        return self.click_点击(self.btn_添加行程_车次查询,"btn_添加行程_车次查询")

    def click_添加行程_输入车次号(self,车次号):
        self.click_点击(self.ipt_添加行程_车次号输入框,"ipt_添加行程_车次号输入框")
        return self.act_键盘输入(车次号)

    def click_点击出发地(self):
        return self.click_点击(self.btn_添加行程_出发地, "点击站站查询_出发地")

    def click_点击目的地(self):
        return self.click_点击(self.btn_添加行程_目的地, "点击站站查询_目的地")

    def click_点击出发日期(self):
        return self.click_点击(self.btn_今天, "点击日期")

    def click_点击跨天日期(self):
        a = self.get_screenSize()
        x = a[0] * 0.5
        y = a[1] - 200
        return TouchAction(self.driver).tap(x=x, y=y).perform()

    def bus_添加行程_输入车次号(self,车次号):
        self.click_添加行程_输入车次号(车次号)
        self.click_添加行程_查询方式("站站添加")
        self.click_添加行程_车次查询()
        self.click_添加行程_查询()
        return 车次号

