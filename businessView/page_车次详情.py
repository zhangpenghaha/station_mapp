from common.loc import *
from businessView.page_车次途经站点 import page_车次途经站点
from common.request import *


class page_车次详情(page_车次途经站点):


    btn_车次详情_分享按钮 = loc_child_IDtoC_Number('com.tencent.mm:id/a0','android.widget.ImageView',0)

    btn_车次详情_行李托运 = loc_text('行李托运')
    btn_车次详情_undefined = loc_contains_text_instance('und',0)
    btn_车次详情_null = loc_contains_text_instance('nu',0)

    def click_车次详情_分享按钮(self):
        return self.click_点击(self.btn_车次详情_分享按钮,'btn_车次详情_分享按钮')

    def get_车次详情_行李托运(self):
        return self.get_元素文本(self.btn_车次详情_行李托运,'btn_车次详情_行李托运')

    def check_车次详情_undefined(self):
        """
        :return: 返回结果正常为11
        """
        a1=self.judge_元素(self.btn_车次详情_undefined)
        a2=self.judge_元素(self.btn_车次详情_null)
        return str(a1)+str(a2)

    def bus_车次详情_行程绑定成功(self):
        """
        :return: 返回结果正常为111
        """
        a1=self.get_车次详情_行李托运()
        a2 =self.check_车次详情_undefined()
        return str(a1)+str(a2)