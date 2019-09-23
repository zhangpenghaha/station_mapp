from businessView.page_首页 import page_首页
from myUnit.st_首页 import st_首页
from businessView.page_车站大屏 import page_车站大屏
import unittest

class Tc_车站大屏详情(st_首页):
    def setUp(self):
        dr =page_首页(self.driver)
        dr.act_上滑()
        dr.click_查看全部车次()
    def test_01_点击车次查看详情文案(self):
        dr = page_车站大屏(self.driver)
        a =dr.get_点击车次查看详情文案()
        self.myEq("点击车次 查看详情",a,"判断文案是否存在")
    def test_02_切换到到达大屏(self):
        dr = page_车站大屏(self.driver)
        dr.click_到达()
        a=dr.get_出站口文案()
        self.myEq("出站口",a,"切换到达到大屏")
    def test_03_切换到候车大屏(self):
        dr = page_车站大屏(self.driver)
        dr.click_候车()
        a=dr.get_检票口文案()
        self.myEq("检票口",a,"切换到候车大屏")
    def test_04_检查输入框文案(self):
        dr = page_车站大屏(self.driver)
        a=dr.get_输入框文案()
        self.myEq("请输入要查询的车次号",a,"检查输入框文案")

     #还没有找到判断是否成功的点
    def test_05_勾选高铁动车(self): #
        dr = page_车站大屏(self.driver)
        dr.click_勾选高铁()

    def test_06_检查以上信息仅供参考文案(self):
        dr = page_车站大屏(self.driver)
        a=dr.get_以上信息仅供参考文案()
        self.myEq("以上信息仅供参考，实际情况以车站公告为准",a,"检查以上信息仅供参考文案")

    def test_07_点击搜索输入框(self):
        dr = page_车站大屏(self.driver)
        dr.click_输入框()
        a = dr.get_键盘元素()
        self.myEq('C',a,"检查键盘是否弹出")
    def test_08_搜索车次(self):
        dr=page_车站大屏(self.driver)
        dr.click_输入框()
        a=dr.click_搜索车次()
        self.myEq("郑州东",a,"搜索车次")

    # 还没有找到判断是否成功的点
    def test_09_清空搜索框(self):
        dr=page_车站大屏(self.driver)
        dr.click_输入框()
        dr.click_搜索车次()
        dr.click_清空输入框()

    def test_010_点击键盘的删除按钮(self):
        dr=page_车站大屏(self.driver)
        dr.click_输入框()
        a =dr.click_键盘删除按钮()
        self.myEq("G7",a,"检查删除按钮")

    def test_012_点击车次查看详情(self):
        dr=page_车站大屏(self.driver)
        a=dr.click_点击车次查看详情()
        self.myEq("前一天",a,"查看车次详情")

if __name__ == '__main__':
    unittest.main
