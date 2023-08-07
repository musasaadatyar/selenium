from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import os
from pathlib import Path

from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(executable_path=r"C:\Program Files\chrom Driver\chromedriver.exe"))
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

# session5 xpath(functions)
#  لازم نیست که مقدار value را کامل بنویسیم بخشی را مینویسیم
# 1: contains(argumant,value) ==> //*[contains(@id,'lna')],//*[contains(text(),'layout two')]

# باید مقدار اول value را وارد کنیم و لازم نیست کامل وارد شود
# 2: start-with(argu, value)] ==> //*[starts-with(@id,'lna')]
# 3: postion() ==> //tr[position()=2]

# به دست آوردن آخرین مقدار
# //tr[last()]

# به دست آوردن یکی مونده به آخر:4
# //tr[last()-1]

# به دست اوردن یک عضو در یک زیرمجموعه:5
# //tr[last()-1]//td[last()-2]

# برای پیدا کردن مقداری استفاده میشود که مقدار مشخصی دارد:6
# //tbody[ count(//tr)=7] , //tbody[ count(.//tr)=7]

# functions ignor case
# برای حذف space های اضافی اول و آخر
# 1: normalize-space ==> //*[ normalize-space ( text())="Option 1" ] , //*[ normalize-space (@id)="moption " ]

# برای پیدا کردن یک المنت و جایگزین کردن آن با یک مقدار خاص
# 2: tranclate(string, str1, dtr2)  ==> //*[translate(@value,"ABCDEFGHIJKLMNOPQRSTYVWXYZ","abcdefghijklmnopqrsdwyz")="option 1"]
# //*[normalize-space(translate(@value,"ABCDEFGHIJKLMNOPQRSTYVWXYZ","abcdefghijklmnopqrsdwyz"))="option 1"]

#پیدا کردن یک مقدار بر اساس طول
# 
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

# sesion6 - xpath(acess)
# به دست آوردن والد
# 1://*[@id='qbc']/parent::*[@id='def'] ==>//*[@id='uname']/parent::div[@class='login form'],//*[@id='uname']/..

# ancestor: درتمام اجداد میگردد
# پیدا کردن اجداد یک المنت تا هرچه قدر که بخواهیم بریم غقب
# 2://*[@id='abc']/ancestor::*[@id='def'] ==> //td[text()='Singer']/ancestor::table[@style='width:100%']

# این المنت پدر و خود فرزند که اون مشخصات داشته باشند را می اورد
# 3: //*[@name='uname']/ancestor-or-self::*[@id='uname']

# پیدا کردن فرزند های یک المنت است
# //tbody/tr[3]/child::*[text()='Singer']

# descendant در تمام نوادگان آن می گردد
# 1: //tag/descendant::*[@id='' ] ==>//tbody/descendant::*[text()='Singer']

# //*[@name='uname']/descendant-or-self::*[@id='uname']

# following  از یک نقط به بعد دنبال آن می گردد
# 1://select[@id='option']/following::*[@value='option 1']

# following-sibling => پیدا کردن المنت هم سطح
# //*[@id='abc123']/following-sebling::*[@value='option 2']

# preceding : المنت های هم سطح که قبل از جای ک مشخص میکنیم
# //*[@id='abc']/preceding-sibling::*[@id='asd']
