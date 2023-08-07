class Login:
# constractor
    def __len__(self, driver):
        self.driver = driver
        self.userName_input_id = 'txtUsername'
        self.password_input_id = 'txtPassword'
        self.login_button_id = 'btnLogin'

    def enter_username(self, username):
        self.driver.find_element('id', self.userName_input_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('id', self.password_input_id).send_keys(password)

    def click_on_login_btn(self):
        self.driver.find_element('id', self.userName_input_id).click()