# -*- coding:utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
class app():

    def __init__(self):
        # 组装设备的字典信息
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # android的apk还是IOS的ipa
        desired_caps['platformVersion'] = '5.1.1'  # android系统的版本号
        desired_caps['deviceName'] = '62001'  # 手机设备名称，通过adb devices  查看
        desired_caps['app'] = r'd:\hgl.apk'  # 安装app
        desired_caps['appPackage'] = 'com.tuols.ipark'  # apk的包名
        desired_caps['appActivity'] = 'com.jz.appframe.ui.activity.LoginActivity'  # apk的launcherActivity
        desired_caps['noReset'] = 'true'  # 不要初始化
        desired_caps['unicodeKeyboard'] = True  # 使用unicodeKeyboard的编码方式来发送字符串
        desired_caps['resetKeyboard'] = True  # 将键盘给隐藏起来
        desired_caps['automationName'] = 'uiautomator2'  #配置识别toast内容
        
        # 连接appium服务
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动服务器地址，后面跟的是手机信息

    def login_pass(self):
        # 动态等待页面的activity加载完成
        time.sleep(3)
        self.driver.find_element_by_id("com.tuols.ipark:id/et_company").clear()
        self.driver.find_element_by_id("com.tuols.ipark:id/et_name").clear()
        self.driver.find_element_by_id("com.tuols.ipark:id/et_pass").clear()
        self.driver.find_element_by_id("com.tuols.ipark:id/et_company").send_keys("dyhd")
        self.driver.find_element_by_id("com.tuols.ipark:id/et_name").send_keys("rbly2")
        self.driver.find_element_by_id("com.tuols.ipark:id/et_pass").send_keys("123456")
        self.driver.find_element_by_id("com.tuols.ipark:id/tv_login").click()
        self.driver.wait_activity("com.jz.appframe.ui.activity.MainActivity",30)

    def login_fail(self):
        # 动态等待页面的activity加载完成
        time.sleep(3)
        self.driver.find_element_by_id("com.tuols.ipark:id/et_company").clear()
        self.driver.find_element_by_id("com.tuols.ipark:id/et_name").clear()
        self.driver.find_element_by_id("com.tuols.ipark:id/et_pass").clear()
        self.driver.find_element_by_id("com.tuols.ipark:id/et_company").send_keys("dyhd")
        self.driver.find_element_by_id("com.tuols.ipark:id/et_name").send_keys("rbly2")
        self.driver.find_element_by_id("com.tuols.ipark:id/et_pass").send_keys("1234567")
        self.driver.find_element_by_id("com.tuols.ipark:id/tv_login").click()
        #获取登录失败的toast消息
        error_message = "登录失败，请检查输入的信息"
        message = "//*[@text=\'{}']".format(error_message)
        '''显示等待WebDriverWait()，一般和until()或until_not()方法配合使用，
        另外，lambda提供了一个运行时动态创建函数的方法。
        '''
        a = WebDriverWait(self.driver,5).until(lambda x:x.find_element_by_xpath(message))
        print(a.text)

    def tongji(self):
        '''
        UIautomator定位是Android系统原生支持的定位方式，和xpath类似，且支持元素的所有属性定位，
        Appium元素定位也是基于Uiautomator进行封装的，so定位也是很强大。
        '''
        #self.driver.find_element_by_android_uiautomator('new UiSelector().text("统计")').click()
        #xpath定位
        #点击统计的text
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'统计')]").click()
        time.sleep(5)
        #需要点击刷新按钮，统计页面的元素才能出现
        self.driver.find_element_by_id("com.tuols.ipark:id/tv_right").click()
        time.sleep(3)
        print(self.driver.current_activity)
        print(self.driver.page_source)
        self.driver.find_element_by_xpath("//android.widget.Spinner[contains(@text,'本日')]").click()
        time.sleep(2)
        print(self.driver.current_activity)
        print(self.driver.contexts)
        self.driver.find_element_by_xpath("//android.widget.CheckedTextView[contains(@text, '本周')]").click()

    def tongzhi(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'通知')]").click()
        time.sleep(1)
        for i in range(2):
            self.swipeDown()
            time.sleep(1)

    def renshi(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'人事')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'智库')]").click()
        WebDriverWait(self.driver,30).until(lambda x:x.find_element_by_class_name("android.webkit.WebView"))
        print(self.driver.contexts)
        #self.driver.switch_to.context('')



    def tongxunlu(self):
        self.driver.find_element_by_id("com.tuols.ipark:id/et_search").click()
        self.driver.activate_ime_engine('com.sohu.inputmethod.sogou/.SogouIME')  # 切换回搜狗输入法,调出键盘,点击搜索
        self.driver.find_element_by_id("com.tuols.ipark:id/et_search").send_keys("任斌")
        #点击右下角的搜索，即ENTER键
        time.sleep(1)
        self.driver.keyevent(66)
        # self.driver.hide_keyboard()
        time.sleep(1)
        self.driver.find_element_by_id("com.tuols.ipark:id/et_search").click()
        self.driver.activate_ime_engine('com.sohu.inputmethod.sogou/.SogouIME')  # 切换回搜狗输入法,调出键盘,点击搜索
        #self.driver.activate_ime_engine('io.appium.settings/.UnicodeIME')  # 切换回自带输入法,调出键盘,点击搜索
        self.driver.find_element_by_id("com.tuols.ipark:id/et_search").send_keys("132")
        #点击右下角的搜索，即ENTER键
        time.sleep(1)
        self.driver.keyevent(66)
        # self.driver.hide_keyboard()

    #获取app屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x,y

    #向下滑动
    def swipeDown(self):
        l = self.get_size()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.1)
        y2 = int(l[1]*0.9)
        self.driver.swipe(x1,y1,x1,y2,1000)



if __name__ == '__main__':
    a = app()
    a.login_pass()
    a.renshi()
