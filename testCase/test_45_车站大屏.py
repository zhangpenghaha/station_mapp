from businessView.page_首页 import page_首页
from myUnit.st_首页 import st_首页
from businessView.page_车站大屏 import page_车站大屏
import unittest

class tc_车站大屏详情(st_首页):
    def setUp(self):
        dr =page_首页(self.driver)
        dr.click_首页()
        dr.act_下滑(3)
        dr.act_滑动_byYourSelf(dr.txt_首页_时刻查询模块名, 0.5, 0.15, "txt_首页_时刻查询模块名移动到0.15位置")
        dr.act_滑动_byYourSelf(dr.btn_首页车站大屏_候车按钮, 0.5, 0.3, "btn_首页车站大屏_候车按钮移动到0.3位置")
        dr.click_查看全部车次()

    def test_001_车站大屏候车字段检查(self):
        dr=page_车站大屏(self.driver)
        a=dr.bus_车站大屏_候车信息检查("候车")
        self.myEq(a,["车次","终到站","发车","检票口","状态"],"test_001_车站大屏候车字段检查")

    def test_002_车站大屏到达字段检查(self):
        dr=page_车站大屏(self.driver)
        a=dr.bus_车站大屏_候车信息检查("到达")
        self.myEq(a,["车次","始发站","到本站","出站口","状态"],"test_001_车站大屏候车字段检查")


    def tearDown(self):
        dr=page_车站大屏(self.driver)
        dr.tc_后置回首页()



if __name__ == '__main__':
    import unittest
    unittest.main()
