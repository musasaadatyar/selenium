from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from archive.classPages.loginPage import Login
from archive.classPages.mainPage import MainPage
import unittest



class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        login_object = Login(driver=self.driver)
        login_object.enter_username('Admin')
        login_object.enter_password('admin123')
        login_object.click_on_login_btn()

    def test_valid_main_page(self):
        main_page_object = MainPage(driver=self.driver)
        main_page_object.check_pain_page()

    def test_invalid_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        login_object = Login(driver=self.driver)
        login_object.enter_username('Admin')
        login_object.enter_password('admin1123')
        login_object.click_on_login_btn()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
