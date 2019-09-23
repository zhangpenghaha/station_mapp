from businessView.page_店铺详情 import page_店铺详情
from common.loc import *
from time import sleep

class page_填写评论(page_店铺详情):
    ipb_填写评论_商家评论 = loc_child_IDtoC_Number("com.tencent.mm:id/y", "android.widget.EditText", 0)
    btn_填写评论_星级 = loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/playStation/pages/write/write.html:VISIBLE",
                                        "android.widget.Image", 3)
    btn_填写评论_提交评价 = loc_child_TtoT("wx8d75e764f0c4bf1c:pages/playStation/pages/write/write.html:VISIBLE", "提交评价 ")
    btn_填写评论_添加图片 = loc_child_TtoT("wx8d75e764f0c4bf1c:pages/playStation/pages/write/write.html:VISIBLE", "添加图片")
    btn_填写评论_勾选匿名 = loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/playStation/pages/write/write.html:VISIBLE",
                                          "android.widget.Image", 7)

    "提示定位"

    def click_填写评论_选择星级(self, startNum):
        return self.click_点击(
            loc_child_TtoC_Number("wx8d75e764f0c4bf1c:pages/playStation/pages/write/write.html:VISIBLE",
                                  "android.widget.Image", {}).format(startNum), "点击" + str(startNum) + "星级")

    def click_填写评论_商家评论(self):
        return self.click_点击(self.ipb_填写评论_商家评论, "btn_商家评论")



    def send_填写评论_商家评论(self, info):
        return self.send_输入(self.ipb_填写评论_商家评论, "ipb_商家评论", info)


    def click_填写评论_提交评价(self):
        return self.click_点击(self.btn_填写评论_提交评价, "btn_提交评价")

    def click_填写评论_添加图片(self):
        return self.click_点击(self.btn_填写评论_添加图片, "btn_添加图片")

    def click_填写评论_勾选匿名(self):
        return self.click_点击(self.btn_填写评论_勾选匿名, "btn_填写评论_匿名")

    def bus_填写评论_流程(self, 勾选匿名=False, 选择星级=None, 评价内容=None, 上传图片=None, 提交评价=True):

        if 勾选匿名 == True:
            self.click_填写评论_勾选匿名()
        if 选择星级 != None:
            self.click_填写评论_选择星级(选择星级)
        if 上传图片 != None:
            list = 上传图片.split("-")
            self.click_填写评论_添加图片()
            self.choose_图片(int(list[0]), int(list[1]))
        if 评价内容 != None:
            self.send_填写评论_商家评论(评价内容)
            self.click_填写评论_商家评论()
        if 提交评价 == True:
            self.click_填写评论_提交评价()


if __name__ == '__main__':
    from appiumDriver.desired_caps import appium_微信车站通
    from businessView.page_切换站点 import page_切换站点
    from businessView.page_店铺详情 import page_店铺详情

    driver = appium_微信车站通()
    dr = page_填写评论(driver)
    dr.click_首页_切换站点按钮()
    dr = page_切换站点(driver)
    dr.bus_切换站点_切换到指定站点("浠水站")
    dr.act_上滑(3)
    dr.click_首页_车站商业进站前1号位()
    dr = page_店铺详情(driver)
    dr.click_店铺详情_评论此商家()
    dr = page_填写评论(driver)
    dr.bus_填写评论_流程(勾选匿名=True, 选择星级=5, 评价内容="好评!", 上传图片="1-1")
