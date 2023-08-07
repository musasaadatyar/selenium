from login import Login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

driver = webdriver.Chrome(service=Service(executable_path=r"C:\Program Files\chrom Driver\chromedriver.exe"))
driver.get('http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login')
driver.implicitly_wait(5)

login_object = Login(driver = driver)
login_object.enter_username('Admin')
login_object.enter_password('admin123')
login_object.click_on_login_btn()