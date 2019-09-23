# coding=utf-8
import logging
import time
import os
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from function.function import path_项目路径
from selenium.webdriver.common.by import By

class baseView(object):
    def __init__(self, driver):
        self.driver = driver

    def get_ele_attribute(self, loc, element, info):
        try:
            WebDriverWait(self.driver, 12).until(lambda x: x.find_element_by_android_uiautomator(loc))
            ele = self.driver.find_element_by_android_uiautomator(loc)
        except TimeoutException:
            logging.error(info + "元素找不到!")
            return 0
        else:
            return ele.get_attribute(element)

    # 单个元素定位，传入元素定位元组
    def find_元素(self, loc, info):
        try:
            WebDriverWait(self.driver, 12).until(lambda x: x.find_element_by_android_uiautomator(loc))
        except TimeoutException:
            logging.error(info + "元素找不到!")
            return 0
        else:
            return self.driver.find_element_by_android_uiautomator(loc)

    def click_点击(self, loc, info):
        logging.info("点击" + info + "!")
        try:
            WebDriverWait(self.driver, 12).until(lambda x: x.find_element_by_android_uiautomator(loc))
            self.driver.find_element_by_android_uiautomator(loc).click()
        except TimeoutException:
            logging.error(info + "元素找不到!")
            return None
        else:
            return True

    def get_context(self):
        return self.driver.contexts

    def switch_to_webView(self, webView):
        return self.driver.switch_to.context(webView)

    def switch_to_NATIVE_APP(self):
        return self.driver.switch_to.context('NATIVE_APP')

    def send_输入(self, loc, info, mes):
        logging.info(info + "输入" + mes + "!")
        try:
            WebDriverWait(self.driver, 12).until(lambda x: x.find_element_by_android_uiautomator(loc))
        except NoSuchElementException:
            logging.error(info + "元素找不到!")
            return 0
        else:
            self.driver.find_element_by_android_uiautomator(loc).send_keys(mes)
            return 1

    def get_元素文本(self, loc, info,timeout=10):
        logging.info("获取" + info + "!")
        try:
            WebDriverWait(self.driver, timeout).until(lambda x: x.find_element_by_android_uiautomator(loc))
            ele = self.driver.find_element_by_android_uiautomator(loc).text
        except Exception as e:
            logging.error(e)
            logging.error(info + "元素找不到!")
            return 0
        else:
            return ele

    def clear_清除(self, loc, info):

        logging.info("清除" + info + "!")
        try:
            WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_android_uiautomator(loc))
            self.driver.find_element_by_android_uiautomator(loc).clear()
        except TimeoutException:
            logging.error(info + "元素找不到!")
            return 0
        else:
            return 1

    def old_click_点击(self, *loc, info):
        logging.info("点击" + info + "!")
        try:
            WebDriverWait(self.driver, 8).until(lambda x: x.find_element(*loc))
            ele = self.driver.find_element(*loc)
        except TimeoutException:
            logging.error(info + "元素找不到!")
            return 0
        else:
            ele.click()
            return 1

    def old_send_输入(self, *loc, info, mes):
        logging.info(info + "输入" + mes + "!")
        try:
            WebDriverWait(self.driver, 8).until(lambda x: x.find_element(*loc))
            ele = self.driver.find_element(*loc)
        except TimeoutException:
            logging.error(info + "元素找不到!")
            return 0
        else:
            ele.send_keys(mes)
            return 1

    def old_get_元素文本(self, *loc, info):
        logging.info("获取" + info + "!")
        try:
            WebDriverWait(self.driver, 8).until(lambda x: x.find_element(*loc))
        except TimeoutException:
            logging.error(info + "文本元素找不到!")
            return 0
        else:
            logging.info(self.driver.find_element(*loc).text)
            return self.driver.find_element(*loc).text

    def old_clear_清除(self, *loc, info):

        logging.info("清除" + info + "!")
        try:
            WebDriverWait(self.driver, 8).until(lambda x: x.find_element(*loc))
            ele = self.driver.find_element(*loc)
        except TimeoutException:
            logging.error(info + "元素找不到!")
            return 0
        else:
            ele.clear()
            return 1

    "系统操作!!!!!!!!!!!!!!!!!!!!"

    def sys_返回键(self):
        logging.info("点击sys_返回键!")
        self.driver.press_keycode(4)

    def sys_关闭app(self):
        logging.info("关闭APP!!!")
        self.driver.close_app()
        self.driver.press_keycode(82)
        WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element(By.ID, "com.huawei.android.launcher:id/clear_all_recents_image_button"))
        self.driver.find_element(By.ID, "com.huawei.android.launcher:id/clear_all_recents_image_button").click()
        os.system("adb kill-server")

    def close(self):
        logging.info("退出小程序和微信!")
        try:
            self.driver.find_element_by_id("com.tencent.mm:id/ot").click()
        except TimeoutException:
            logging.error("没有找到退出小程序的元素!")
            self.driver.close_app()
        else:
            self.driver.close_app()

    # 获取多个元素集，传入元素定位元组
    def find_多个元素列表(self, *loc):
        return self.driver.find_elements(*loc)

    # 获取窗口尺寸，返回列表[x，y]
    def get_窗口尺寸(self):
        return self.driver.get_window_size()

    # 滑动操作，传入起始坐标点，和滑动持续时间（单位秒）
    def act_滑动(self, start_x, start_y, end_x, end_y, duration):
        x1 = int(start_x)
        x2 = int(end_x)
        y1 = int(start_y)
        y2 = int(end_y)
        time = duration * 1000
        return self.driver.swipe(x1, y1, x2, y2, time)

    # 点击操作
    def act_点击(self, positions, duration):

        return

    # 显示等待
    def wait_显式等待(self, time, loc):
        try:
            WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_android_uiautomator(loc))
        except TimeoutException:
            logging.error("页面加载失败!")
            return 0
        else:
            logging.info("页面加载成功!")
            return 1

    # 判断元素是否存在
    """
    @parameter:时间(等待时间)和定位器(Ui Selector)
    
    @return: 返回0元素不存在,返回1元素存在
    """

    def judge_元素(self,loc):
        try:
            self.driver.find_element_by_android_uiautomator(loc)
        except Exception as e:
            logging.error(e)
            logging.error(loc + "judge_元素不存在!")
            return 0
        else:
            return 1

    # 隐士等待
    def wait_隐式等待(self, time):
        return self.driver.implicitly_wait(time)

    # 获取当前时间
    def fun_获取时间戳(self):
        return time.strftime("%Y-%m-%d %H_%M_%S")

    # 截图,传入模块名称
    def fun_截图(self, 模块名):
        name = 模块名 + "_" + self.fun_获取时间戳()
        image_file = path_项目路径() + r"\screenShots\{}.png".format(name)
        logging.info("截取 {} 图片 ".format(模块名))
        self.driver.get_screenshot_as_file(image_file)

    def tapT(self, xt, yt):
        x_1 = xt / 1080  # 780 / 1080
        y_1 = yt / 2060  # 2230 / 2060
        x = driver.get_window_size()['width']  # 获取设备的屏幕宽度
        y = driver.get_window_size()['height']  # 获取设备屏幕的高度
        print(x)
        print(y)
        print(x_1 * x, y_1 * y)  # 打印出点击的坐标点
        driver.close_app()
        driver.tap([(x_1 * x, y_1 * y)], 500)  # 模拟单手点击操作
        driver.find_element_by_id("com.huawei.android.launcher:id/clear_all_recents_image_button").click()

    def scroll_page_one_time( self, direction="up" ):
        """
        滑动一次屏幕
        :param direction: 方向
            "up"：从下往上
            "down"：从上往下
            "right"：从左往右
            "left"：从右往左
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        center_x = width / 2
        center_y = height / 2

        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y

        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    def find_element_with_scroll( self, feature, direction="up" ):
        """
        边滑边找 某个元素的特征
        :param feature: 元素的特征
        :param direction: 方向
            "up"：从下往上
            "down"：从上往下
            "right"：从左往右
            "left"：从右往左
        :return:
        """
        page_source = ""
        while True:
            try:
                return self.loc_text(feature)
            except Exception:

                self.scroll_page_one_time(direction)

                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source


if __name__ == '__main__':
    from time import sleep
    from appiumDriver.desired_caps import appium_微信车站通

    while 1:
        driver = appium_微信车站通()
        driver.tapT(790, 2060)
