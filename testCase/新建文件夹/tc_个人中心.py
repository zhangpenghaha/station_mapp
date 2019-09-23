from myUnit.st_首页 import st_首页
from businessView.page_个人中心 import page_个人中心
from businessView.page_我的资料 import page_我的资料
from businessView.page_我的积分 import page_我的积分
from businessView.page_登录12306 import page_登录12306


class tc_个人中心(st_首页):

    def setUp(self):
            dr = page_个人中心(self.driver)
            dr.click_我的按钮()

    def test_2_我的页面跳转(self):
        dr = page_个人中心(self.driver)
        a = dr.get_意见反馈()
        self.myEq("意见反馈", a, "个人中心跳转")

    def test_3_我的资料跳转(self):
        dr = page_我的资料(self.driver)
        dr.click_头像区()
        a = dr.get_text_您的手机号()
        self.myEq("您的手机号", a, "我的资料跳转")

    def test_4_我的积分跳转(self):
        dr=page_我的积分(self.driver)
        dr.click_我的积分_下()
        a=dr.get_做任务领积分()
        self.myEq("做任务领积分",a,"我的积分页面跳转")

    def test_5_我的12306跳转(self):
        dr=page_登录12306(self.driver)
        dr.click_我的12306()
        a=dr.get_登录12306按钮()
        self.myEq("登录12306",a,"我的12306跳转")


    def tearDown(self):
        dr = page_个人中心(self.driver)
        dr.tc_后置回首页()


if __name__ == '__main__':
    import unittest
    unittest.main()
