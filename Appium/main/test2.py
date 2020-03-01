# -*- coding:utf-8 -*-
from appium import webdriver
import time

#组装设备的字典信息
desired_caps={}
desired_caps['platformName']='Android' #android的apk还是IOS的ipa
desired_caps['platformVersion']='5.1.1' #android系统的版本号
desired_caps['deviceName']='62001'  #手机设备名称，通过adb devices  查看
desired_caps['app']=r'd:\hgl.apk'   #安装app
desired_caps['appPackage']='com.tuols.ipark'   #apk的包名
desired_caps['appActivity']='com.jz.appframe.ui.activity.LoginActivity'   #apk的launcherActivity
desired_caps['noReset']='true'   #不要初始化
desired_caps['unicodeKeyboard'] = True   #使用unicodeKeyboard的编码方式来发送字符串
desired_caps['resetKeyboard'] = True   #将键盘给隐藏起来

#连接appium服务
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)  #启动服务器地址，后面跟的是手机信息
# 动态等待页面的activity加载完成
driver.wait_activity("com.jz.appframe.ui.activity.LoginActivity",30)
driver.find_element_by_id("com.tuols.ipark:id/et_company").clear()
driver.find_element_by_id("com.tuols.ipark:id/et_name").clear()
driver.find_element_by_id("com.tuols.ipark:id/et_pass").clear()
driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @index='2']").send_keys("dyhd")




# driver.find_element_by_id("com.tuols.ipark:id/et_search").click()
# driver.activate_ime_engine('com.sohu.inputmethod.sogou/.SogouIME')  # 切换回搜狗输入法,调出键盘,点击搜索
# driver.find_element_by_id("com.tuols.ipark:id/et_search").send_keys("任斌")
# #点击右下角的搜索，即ENTER键
# time.sleep(1)
# driver.keyevent(66)
# # driver.hide_keyboard()
# time.sleep(1)
# driver.find_element_by_id("com.tuols.ipark:id/et_search").click()
# driver.activate_ime_engine('com.sohu.inputmethod.sogou/.SogouIME')  # 切换回搜狗输入法,调出键盘,点击搜索
# #driver.activate_ime_engine('io.appium.settings/.UnicodeIME')  # 切换回自带输入法,调出键盘,点击搜索
# driver.find_element_by_id("com.tuols.ipark:id/et_search").send_keys("132")
# #点击右下角的搜索，即ENTER键
# time.sleep(1)
# driver.keyevent(66)
# # driver.hide_keyboard()

# 卸载应用
#driver.remove_app('com.tuols.ipark')