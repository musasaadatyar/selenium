from archive.locator.loators import *


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('xpath', userName_input_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('xpath', password_input_xpath).send_keys(password)

    def click_on_login_btn(self):
        self.driver.find_element('xpath', login_button_xpath).click()
