from baseView.base_excel import read_excel
from businessView.page_始发站选择 import page_选择车次出发和到达
from businessView.page_选择城市 import Page_选择城市
from businessView.page_选择日期 import page_选择日期
from businessView.page_选择车次 import page_选择车次
from myUnit.st_首页 import st_首页
from businessView.page_行程 import page_行程
from businessView.page_添加行程 import page_添加行程
from parameterized import parameterized


class Test_行程(st_首页):
    def setUp(self):
        dr = page_行程(self.driver)
        dr.click_点击行程()

    @parameterized.expand(read_excel("test_data.xlsx", "checichaxun"))
    def test_2_手动添加行程_车次查询(self, test_车次, test_data, test_起始站, test_终点站,  if_success, test_toast):
        dr = page_行程(self.driver)
        dr.click_点击行程()
        dr.click_行程_添加行程()
        dr.click_行程_手动添加()
        dr = page_添加行程(self.driver)
        dr.click_添加行程_查询方式("车次查询")
        dr.send_输入车次(test_车次)
        dr.click_点击出发日期()
        dr = page_选择日期(self.driver)
        dr.click_选择几天后日期(test_data)
        dr = page_添加行程(self.driver)
        dr.click_添加行程_查询()
        if if_success == "error_车次":
            a = dr.get_toast(test_toast)
            dr.click_确定()
            self.myEq(test_toast, a, "test车次查询输入错误的车次")
        if if_success == "success":
            dr = page_选择车次出发和到达(self.driver)
            dr.btn_选择起始站(test_起始站)
            dr.btn_选择终点站(test_终点站 )
            dr.click_确定添加()
            a = dr.get_toast(test_toast)
            self.myEq(test_toast, a, "test车次查询绑定正确车次")



    @parameterized.expand(read_excel("test_data.xlsx", "zhanzhanchaxun"))
    def test_3_手动添加行程_站站查询( self, test_出发地, test_目的地 , test_days, test_车次, if_success, test_toast):
        dr = page_行程(self.driver)
        dr.click_点击行程()
        dr.click_行程_添加行程()
        dr.click_行程_手动添加()
        dr = page_添加行程(self.driver)
        dr.click_添加行程_查询方式("站站查询")
        dr.click_点击出发地()
        if if_success == "success":
            dr = Page_选择城市(self.driver)
            dr.select_选择城市(test_出发地)
            dr.click_点击目的地()
            dr.select_选择城市(test_目的地)
            dr.click_点击出发日期()
            dr = page_选择日期(self.driver)
            dr.click_选择几天后日期(test_days)
            dr = page_添加行程(self.driver)
            dr.click_添加行程_查询()
            dr= page_选择车次(self.driver)
            dr.click_点击车次(test_车次)
            dr.click_确认添加()
            a = dr.get_toast(test_toast)
            self.myEq(test_toast, a, "test站站查询绑定正确车次")
        if if_success == "error_城市搜索框":
            dr = Page_选择城市(self.driver)
            dr.click_点击城市搜索框()
            dr.send_输入(test_出发地)
            a = dr.get_toast(test_toast)
            self.myEq(test_toast, a, "test站站查询城市搜索输入错误")

    def test_5_删除行程( self ):
        dr = page_行程(self.driver)
        dr.bus_行程_删除全部(20)  # 输入删除个数
        a = dr.get_行程_添加行程()
        self.myEq(a, "+添加行程", "test_删除全部行程")


    def tearDown(self):
        dr = page_行程(self.driver)
        dr.tc_后置回首页()

if __name__ == '__main__':
    import unittest
    unittest.main()