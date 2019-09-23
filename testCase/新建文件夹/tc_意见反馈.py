from myUnit.st_首页 import st_首页
from businessView.page_意见反馈 import page_意见反馈


class tc_意见反馈(st_首页):

    def setUp(self):
        dr = page_意见反馈(self.driver)
        dr.click_我的按钮()
        dr.click_意见反馈()

    def test_202_详细描述和联系方式都为空给出提示(self):
        dr = page_意见反馈(self.driver)
        dr.bus_提交意见反馈("服务体验","","")
        dr.click_提交反馈()
        a1=dr.get_提示信息()
        a2=dr.click_确认()
        a3=dr.click_问题反馈()
        a=str(a1)+str(a2)+str(a3)
        self.myEq("请输入详细描述11",a,"详细描述和联系方式都为空给出提示")

    def test_203_仅详细描述为空给出提示(self):
        dr = page_意见反馈(self.driver)
        dr.bus_提交意见反馈("服务体验","","17702731500")
        dr.click_提交反馈()
        a1=dr.get_提示信息()
        a2=dr.click_确认()
        a3=dr.click_问题反馈()
        a=str(a1)+str(a2)+str(a3)
        self.myEq("请输入详细描述11",a,"详细描述和联系方式都为空给出提示")

    def tearDown(self):
        dr = page_意见反馈(self.driver)
        dr.tc_后置回首页()

if __name__ == '__main__':
    import unittest
    unittest.main()