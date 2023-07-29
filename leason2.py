from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import os
from pathlib import Path

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(executable_path=r"C:\Program Files\chrom Driver\chromedriver.exe"))
driver.get('https://labtob.ir/')

# how to right javaScript code
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# getScreenShot
currentPath = Path(__file__).parents
fileName = os.path.join(str(currentPath), 'session2.png')
driver.save_screenshot(fileName)
sleep(3)

