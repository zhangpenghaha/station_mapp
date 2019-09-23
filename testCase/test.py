from common.desired_caps import appium_desired
from appium import webdriver
from time import sleep
dr = appium_desired()
sleep(6)
a = dr.contexts
print(a)
dr.implicitly_wait(10)
# WEBVIEW_com.tencent.mm:appbrand0 WEBVIEW_com.tencent.mm
dr.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
cc = dr.current_context
print(cc)
dr.implicitly_wait(20)
ah = dr.window_handles
ch = dr.current_window_handle
print(ah)
print(ch)
for handle in ah:
    if handle != ch:
        dr.switch_to.window(handle)
        print(handle)
# print(dr.page_source)
dr.find_element_by_xpath('//*[text()="余票查询"]').click()
sleep(5)
a=dr.window_handles
print(a)
for i in a:
    dr.switch_to.window(i)
    print(i)
    print(dr.title)
    if dr.title =="wx8d75e764f0c4bf1c:page/station/pages/spareTicket/spareTicket.html:VISIBLE":
        break
print(dr.page_source)
# dr.switch_to.window(dr.window_handles[-1])
# print(dr.window_handles[-1])
# print(dr.page_source)
# dr.find_element_by_xpath('//div[@style=\'background-size: 100% 100%; background-repeat: no-repeat; background-image: url("image/switch@2x.png");\']').click()
# dr.find_element_by_xpath('//svg[@viewBox=\'0 0 20 20\']').click()
# dr.find_element_by_css_selector("#block1 > div > div > div.rmd-good-look__comment-box > div > div.rmd-good-look__friend-list > i > svg").click()
dr.find_element_by_xpath('//*[text()="查询"]').click()