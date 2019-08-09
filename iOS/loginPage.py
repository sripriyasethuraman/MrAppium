
import unittest
from appium import webdriver


class Login(unittest.TestCase):

    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'login'

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        # self.dc['udid'] = '9FA70C1C-29E8-4082-A532-50AC39E23A31'
        self.dc['udid'] = '4F562070-3BE3-4C9D-B61D-63507B1ABD20'
        self.dc['deviceName'] = 'iPhone 8'
        self.dc['automationName'] = 'XCUITest'
        self.dc['app'] = '/Users/sripriya/Library/Developer/Xcode/DerivedData/mrios-fkwgfbcwveyjojestdahfdhgsqgs/Build/Products/Debug-iphonesimulator/mrios.app'
        self.dc['platformName'] = 'ios'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def test_Already_registered_Login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("Already registered? Log in").click()
        self.driver.find_element_by_id("Enter your email address").send_keys("sripriya+ios@myrecovery.ai")
        self.driver.find_element_by_id("Enter your password").send_keys("foofoofoo")
        self.driver.find_element_by_id("loginButton").click()
        self.driver.find_element_by_id("OK").click()
        actual_value = self.driver.find_element_by_id("More").text
        self.assertEqual(actual_value, "More")
        #self.driver.find_element_by_id("Tell us about your hip before your operation").click()
        #self.driver.find_element_by_id("OK, thank you").click()
        #self.driver.find_element_by_id("").click()

    def test_Register(self):
        self.driver.find_element_by_id("Register").click()
        self.driver.find_element_by_id("Enter your email address").send_keys("jonny+bulkinvite@myrecovery.ai")
        self.driver.find_element_by_id("Enter your 6-digit pin code").send_keys("718643")
        self.driver.find_element_by_id("Choose a password").send_keys("foofoofoo")
        self.driver.find_element_by_id("Re-enter your password").send_keys("foofoofoo")
        self.driver.find_element_by_id("registerButton").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("OK").click()
        self.driver.find_element_by_id("Progress").click()
        actual_value = self.driver.find_element_by_id("More").text
        self.assertEqual(actual_value, "More")
        #self.driver.find_element_by_id("Info").click()
        #self.driver.find_element_by_id("More").click()

    def test_Ive_forgotten_myPassword(self):
        self.driver.find_element_by_id("Already registered? Log in").click()
        self.driver.find_element_by_id("I've forgotten my password").click()
        self.driver.find_element_by_name("forgotEmailTextField").send_keys("demo@test.mr")
        self.driver.find_element_by_id("Reset password").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

