from common.loc import *
from businessView.page_首页 import page_首页



class page_选择车次(page_首页):
    # 站站查询选择车次

    title_选择车次=loc_text("选择车次")
    date_日期=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/findStation/findStation.html:VISIBLE","android.view.View",1)
    img_高铁动车=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/findStation/findStation.html:VISIBLE","android.widget.Image",1)
    text_共XX车次=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/findStation/findStation.html:VISIBLE","android.view.View",5)
    text_武汉到北京=loc_text("武汉-北京")
    img_日历icon = loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/findStation/findStation.html:VISIBLE",
                                     "android.widget.Image", 0)
    text_选择日期=loc_text("选择日期")
    text_点击日期 = loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/calendar/calendar.html:VISIBLE","android.view.View",24)

    text_底线 = loc_text("— 我也是有底线的 —")

    txt_选择车次_出发地_目的地=loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/station/pages/findStation/findStation.html:VISIBLE","android.view.View",4)
    #结果页

    # text_结果页=loc_text("K600 武昌-北京西")
    text_到达正点率=loc_text("到达正点率")
    text_正点率=loc_text("正点率")
    text_展开=loc_text("展开")
    text_收起 =loc_text("收起")
    text_前序站=loc_text("7个前序站")
    text_后序站 = loc_text("7个后序站")
    text_添加行程文案 = loc_text("添加行程，列车动态实时提醒")
    text_确定添加 = loc_text("确定添加")

    #行程详情页面
    text_全程预计剩余=loc_text("全程预计剩余")


    def get_选择车次_出发地_目的地(self):
        return self.get_元素文本(self.txt_选择车次_出发地_目的地,"txt_选择车次_出发地_目的地")

    def get_选择车次(self):
        return self.get_元素文本(self.title_选择车次,"title_选择车次")

    def get_当前日期(self):
        return self.get_元素文本(self.date_日期,"date_日期")

    def click_勾选高铁动车(self):
        self.click_点击(self.img_高铁动车, 'img_高铁动车')
        return self.get_元素文本(self.text_共XX车次,"text_共XX车次")

    def text_武汉到北京文案(self):
        return self.get_元素文本(self.text_武汉到北京,"text_武汉到北京")

    def click_日历icon(self):
        self.click_点击(self.img_日历icon,"img_日历icon")
        return self.get_元素文本(self.text_选择日期,"text_选择日期")

    def click_今天(self):
        self.click_点击(self.text_点击日期,"text_点击日期")
        return self.get_元素文本(self.date_日期,"date_日期")


#######################################################################################
    def click_点击车次(self, text):
        text_车次 = self.find_element_with_scroll(text)
        self.click_点击(text_车次,"text_车次")
        text_结果页 = loc_text(text)
        return self.get_元素文本(text_结果页,"text_结果页")
#######################################################################################
        # 结果页
    def click_到达正点率(self):
        self.click_点击(self.text_到达正点率,"text_到达正点率")
        return self.get_元素文本(self.text_正点率,"text_正点率")

    def click_展开(self):
        self.click_点击(self.text_展开,"text_展开")
        return self.get_元素文本(self.text_收起,"text_收起")
    def get_前序站(self):
        return self.get_元素文本(self.text_前序站,"text_前序站")
    def get_后序站(self):
        # self.act_上滑()
        return self.get_元素文本(self.text_后序站,"text_后序站")

    def get_添加行程文案(self):
        return self.get_元素文本(self.text_添加行程文案, "text_添加行程文案")

    def click_确定添加(self):
        self.click_点击(self.text_确定添加, "text_确定添加")
        return self.get_元素文本(self.text_全程预计剩余, "text_全程预计剩余")






if __name__ =="__main__":

    from appiumDriver.desired_caps import appium_微信车站通
    from function.funcdate import get_当前月日, get_获取当前星期
    driver=appium_微信车站通()
    dr=page_首页(driver)
    dr.click_站站查询()
    dr.click_时刻查询_查询()
    dt=page_选择车次(driver)
    dt.click_点击车次()
    a=dt.click_确定添加()

    print(a)






