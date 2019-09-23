from myUnit.st_首页 import st_首页
import logging
from businessView.page_首页 import page_首页
import sys
sys.setrecursionlimit(5000)

class tt(st_首页):
    def test_001(self):
        logging.info("我是001!")

    def test_002(self):
        logging.info("我是002!")

    def test_003(self):
        logging.info("我是003!")
        dr =page_首页(self.d)
        dr.click_车站大屏()

