class Login:
# constractor
    def __len__(self, driver):
        self.driver = driver
        self.userName_input_xpath = "//input[@name='username']"
        self.password_input_xpath = "//input[@name='password']"
        self.login_button_xpath = "//button[@type='submit']"

    def enter_username(self, username):
        self.driver.find_element('xpath', self.userName_input_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('xpath', self.password_input_id).send_keys(password)

    def click_on_login_btn(self):
        self.driver.find_element('xpath', self.userName_input_id).click()