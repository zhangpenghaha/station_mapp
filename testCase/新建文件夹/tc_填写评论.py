from myUnit.st_首页 import st_首页
from businessView.page_填写评论 import page_填写评论
from function.function import get_flag,update_flag
import logging
import threading


class tc_填写评论(st_首页):



    def setUp(self):
        dr = page_填写评论(self.driver)
        flag=get_flag()
        if flag==0:
            dr.act_上滑(2)
            dr.click_小胡鸭()
            dr.click_评论此商家()
            update_flag(1)
        else:
            dr.click_小胡鸭()
            dr.click_评论此商家()

    def test_001_全部为空提示(self):
        dr=page_填写评论(self.driver)
        dr.click_提交评价()
        a=dr.get_toast()
        logging.info("toast提示为:"+a)
        self.myEq("描述不能为空",a,"全部为空提示")

    def test_002_评分为空提示(self):
        dr=page_填写评论(self.driver)
        dr.send_商家评论("好吃好吃!!!")
        dr.click_提交评价()
        a= dr.get_toast()
        logging.info("toast提示为:"+a)
        self.myEq("评分不能为空",a,"评分为空提示")

    def test_003_评论为空提示(self):
        dr=page_填写评论(self.driver)
        dr.click_三星()
        dr.click_提交评价()
        a = dr.get_toast()
        logging.info("toast提示为:"+a)
        self.myEq("描述不能为空",a,"评论为空提示")

    def tearDown(self):
        dr=page_填写评论(self.driver)
        dr.tc_后置回首页()

if __name__ == '__main__':
    import unittest
    unittest.main()