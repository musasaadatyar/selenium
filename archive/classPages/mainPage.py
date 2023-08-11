from archive.locator.loators import *


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_label_path = dashboard_label_path

    def check_pain_page(self):
        self.driver.find_element('xpath', dashboard_label_path)
