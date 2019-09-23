from common.common import common
from selenium.webdriver.common.by import By


class page_检票口 (common):

    "定位"

    "文本"
    txt_老弱病残检票口=(By.XPATH,'//*[@text="老弱病残孕软席军人团体检票口"]')



    "获取文本"
    def get_检票口1(self):
        self.get_元素文本(*self.txt_老弱病残检票口,info="txt_老弱病残检票口")


