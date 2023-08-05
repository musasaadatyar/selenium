from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import os
from pathlib import Path

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(executable_path=r"C:\Program Files\chrom Driver\chromedriver.exe"))
driver.get('https://www.wikipedia.org/')
# find element in the page
# 1: id =>
# driver.find_element('id', 'searchInput').send_keys('ایران')
# 2" xpath
# driver.find_element('xpath', '//button[@type="submit"]').click()
# 3: text
# driver.find_element('xpath', "//*[text()='فارسی']").click()
# 4:tag
# driver.find_element('tag name', 'select').click();
# 5:link text
# driver.find_element('link text', 'Download Wikipedia for Android or iOS').click()
# 6 :partial link text
# driver.find_element('partial link text', 'Download').click()
# 7 : class
# driver.find_element('class name', 'svg-search-icon').click()
# 8: css selector for id
# driver.find_element('css selector', '#searchInput').send_keys('selenium')
# 9: css selector for class
# driver.find_element('css selector', '.svg-search-icon').click()
# sleep(9)

# losone4: XPATH
# 1: make xpath ==> //tagname[@atrebiut="value"] , //tagname[text()="value"]
# 2: merge tow xpath => //tag[(condition1 Or condition2) and condition3]
# //*[@class="login form"]//*[@value="Login"]
# 3:find by index xpath ==> //tag[condition1][index], (//tag[condition1])[index],//tag[tag[condition1]] ,//tag[.//tag[condition1]],

 # پیدا کردن یک مقدار با رند کردن آن
 # round: //*[round(text())='435']

# پیدا کردن یک مقدار با رند کردن آن دیگر مقدار اعشار را در نظر نمیگیرد
# floor: //*[floor(text())='432']

# اگر بخواهیم شرطیرا مخالف آن در نظر بگیریم
# not: => //*[@type="radio" and not(@id="male")]

# پیدا کردن مقدار قبل از یک المنت
# substring-before ==> //*[substring(text(),':')='username']
# پیدا کردن مقدار بعد از آن
# substring-after ==> //*[substring(text(),':')='test']
