from appium import webdriver
import time


desired_cups = {}
desired_cups['platformName'] = 'ios'
desired_cups['platformVersion'] = '12.1'
desired_cups['deviceName'] = 'iPhone XR'
desired_cups['automationName'] = 'XCUITest'
desired_cups['udId'] = '4D79C6F5-368B-4035-B83'
desired_cups['bundleId'] = 'com.dealuck.cyyapp'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_cups)
time.sleep(3)

# 首先点击我的
# driver.find_element_by_name("我的")
# driver.find_elements_by_xpath('//XCUIElemetTypeButton[@name="我的"]')

x = driver.get_window_size()
# y = driver.get_window_size()['height']
print(x['width'],x['height'])



# 有问题
driver.tap([(390,833)],200)
print('点击我的ok')



time.sleep(3)
print('点击二维码')
driver.find_element_by_accessibility_id("nav qrCode").click()
print('点击完成')

time.sleep(2)
# 207   655
print('点X返回')
driver.tap([(207,655)])
print('ok')


time.sleep(2)
driver.quit()








