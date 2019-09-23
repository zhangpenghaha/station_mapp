from businessView.page_首页 import page_首页
from function.function import *
from myUnit.st_首页 import st_首页
from businessView.page_车次详情 import page_车次详情
from businessView.page_切换站点 import page_切换站点
from businessView.page_行程 import page_行程

class tc_车次详情(st_首页):

    def setUp(self):
        dr = page_行程(self.driver)
        dr.click_首页()
        dr = page_车次详情(self.driver)
        if dr.get_首页顶部_当前站点()!= "浠水站":
            dr.click_首页_切换站点按钮()
            dr = page_切换站点(self.driver)
            dr.bus_切换站点_切换到指定站点("浠水站")

    def test_500_首页车次号搜索绑定行程(self):
        dr = page_车次详情(self.driver)
        dr.act_下滑(3)
        dr.click_首页_车次查询()
        sid= dr.bus_首页_车次号搜索("G1991")
        dr.bus_选择始终站(sid)
        dr.click_车次途经站点_确认添加()
        a = dr.bus_车次详情_行程绑定成功()
        self.myEq(a,"行李托运00","test_500_首页车次号搜索绑定行程")

    def test_501_行程车次号搜索绑定行程(self):
        dr = page_车次详情(self.driver)
        dr.click_行程()
        dr.bus_行程_手动添加()
        sid= dr.bus_添加行程_输入车次号("G1848")
        dr.bus_选择始终站(sid,点击确认添加=True)
        dr.click_车次途经站点_确认添加()
        a = dr.bus_车次详情_行程绑定成功()
        self.myEq(a,"行李托运00","test_501_行程车次号搜索绑定行程")

    def test_502_首页删除行程(self):
        dr = page_行程(self.driver)
        dr.click_行程()
        a=dr.check_行程_删除行程()
        self.myEq(str(a),"1","test_502_首页删除行程")

    def tearDown(self):
        dr=page_车次详情(self.driver)
        dr.tc_后置回首页()

if __name__ == '__main__':
    import unittest
    unittest.main()