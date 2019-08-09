import unittest
from appium import webdriver


class Android(unittest.TestCase):
    dc = {
        "platformName": "Android",
        "platformVersion": "7.1.1",
        "deviceName": "emulator-5554 ",
        "appPackage": "fhw.com.myrecovery",
        "app": "/Users/sripriya/dev/mr-mobile/android/"
               "app/build/outputs/apk/myrecovery/release/app-myrecovery-release.apk",
        "automationName": "uiAutomator2",
        "appWaitActivity": "fhw.com.myrecovery.launch.LaunchActivity"
    }

    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.dc)

    def test_Already_registered_Login(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("loginSubtitledButton").click()
        self.driver.find_element_by_xpath('//*[@text="Enter your email address"]').send_keys("corin_jhel-throb@test.mr")
        self.driver.find_element_by_xpath("//*[@text='Enter your password']").send_keys("foofoofoo")
        self.driver.find_element_by_id('loginButton').click()
        self.driver.find_element_by_xpath('//*[@text="OK"]').click()
        asserthome = self.driver.find_element_by_xpath('//*[@text="Home"]').text
        self.assertEqual("Home", asserthome)
        self.driver.find_element_by_xpath('//*[@text="More"]')
        self.driver.find_element_by_xpath('//*[@text="Log out"]').click()
        self.driver.find_element_by_xpath('//*[@text="Yes"]').click()

    def test_Ive_forgotten_my_Password(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("loginSubtitledButton").click()
        self.driver.find_element_by_id('forgotPasswordLink').click()
        self.driver.find_element_by_xpath('//*[@text="Enter email address"]').send_keys("corin_jhel-throb@test.mr")
        self.driver.find_element_by_id('resetPasswordButton').click()

    def test_Register(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('registerSubtitledButton').click()
        self.driver.find_element_by_xpath('//*[@text="Enter your email address"]').send_keys("jonny+bulkinvite@myrecovery.ai")
        self.driver.find_element_by_xpath("//*[@text='Enter your 6-digit pin code']").send_keys("718643")
        self.driver.find_element_by_xpath('//*[@text="Choose a password"]').send_keys("foofoofoo")
        self.driver.find_element_by_xpath('//*[@text="Re-enter your password"]').send_keys("foofoofoo")
        self.driver.find_element_by_id('registerButton').click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()