from businessView.page_首页 import page_首页
from myUnit.st_首页 import st_首页
from businessView.page_选择车次 import page_选择车次
import unittest
import time
from function.funcdate import get_当前月日,get_获取当前星期


class tc_首页_时刻查询(st_首页):
    def setUp(self):
        dr =page_首页(self.driver)
        dr.click_首页_站站查询()
        dr.click_首页_时刻查询_查询()

    def test_01_选择车次页面标题(self):
        dr =page_选择车次(self.driver)
        a =dr.get_选择车次()
        self.myEq(a,"选择车次","检查选择车次页面标题")

    def test_02_当前日期(self):
        today = get_当前月日()+" "+get_获取当前星期()
        dr =page_选择车次(self.driver)
        a =dr.get_当前日期()
        self.myEq(today,a,"检查当天日期")

    def test_03_勾选高铁动车(self):
        dr = page_选择车次(self.driver)
        a=dr.click_勾选高铁动车()
        self.myEq("共34车次",a,"勾选高铁动车")

    def test_04_武汉到北京文案(self):
        dr = page_选择车次(self.driver)
        a=dr.text_武汉到北京文案()
        self.myEq("武汉-北京",a,"检查武汉-北京文案")

    def test_05_点击日历icon(self):
        dr =page_选择车次(self.driver)
        a =dr.click_日历icon()
        self.myEq("选择日期",a,"点击日历icon")

    def test_06_选择日期(self):
        dr =page_选择车次(self.driver)
        dr.click_日历icon()
        today = get_当前月日() + " " + get_获取当前星期()
        a=dr.click_今天()
        self.myEq(today,a,"选择今天日期")


    def test_07_点击车次(self):
        dr =page_选择车次(self.driver)
        a =dr.click_点击车次()
        self.myEq("K600 武昌-北京西",a,"点击车次进入结果页")

    # 结果页
    def test_08_跳转正点率(self):
        dr = page_选择车次(self.driver)
        dr.click_点击车次()
        a=dr.click_到达正点率()
        self.myEq("正点率",a,"跳转到正点率页面")
    def test_09_点击展开(self):
        dr = page_选择车次(self.driver)
        dr.click_点击车次()
        a =dr.click_展开()
        self.myEq("收起",a,"点击展开")
    def test_10_检查前序站(self):
        dr = page_选择车次(self.driver)
        dr.click_点击车次()
        a=dr.get_前序站()
        self.myEq("7个前序站",a,"检查前序站")
    def test_11_检查后序站(self):
        dr = page_选择车次(self.driver)
        dr.click_点击车次()
        a=dr.get_后序站()
        self.myEq("7个后序站",a,"检查后序站")
    def test_12_添加行程文案(self):
        dr = page_选择车次(self.driver)
        dr.click_点击车次()
        a = dr.get_添加行程文案()
        self.myEq("添加行程，列车动态实时提醒", a, "检查添加行程，列车动态实时提醒文案")
    def test_13_确定添加(self):
        dr = page_选择车次(self.driver)
        dr.click_点击车次()
        a =dr.click_确定添加()
        self.myEq("全程预计剩余",a,"点击确认添加按钮添加行程")


if __name__ == "__main__":
    import unittest
    unittest.main()
