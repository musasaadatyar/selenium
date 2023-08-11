from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService

# # برای این که درایور مربوط به هر کروم را دانلود کند از این کد استفاده می کنیم اگر فیلتر نباشد
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# برای ادرس دادن محل درایور در selenium v4
driver = webdriver.Chrome(service=ChromeService(executable_path=r"C:\Program Files\chrom Driver\chromedriver.exe"))

# بازکردن یک سایت
# browser action1 > open web
driver.get('https://www.google.com/')

# به دست آوردن تایتل یک صفحه
# browser action2 > title page
# window_title = driver.title

# بازگشت به صفحه قبل
# browser action3 > back page
# driver.back()


# انتقال دوباره از صفحه back به جلو
# browser action4 > forward
# driver.forward()

# refresh کردن صفحه
# browser action5 > refresh
# driver.refresh()

# بازکردن پنجره جدید در صفحه جدید
# open new windows
# browser action6 > open new window and switch to it(tab)
# driver.switch_to.new_window('tab')


# بازکردن پنجره جدید در مرورگر جدید
# browser action7 > open new window and switch to it( window)
# driver.switch_to.new_window('window')
# driver.get('https://labtob.ir/')

# browser action8 > Current window
# یک آیدی از صفحه جدید میدهد
# labtobWindow = driver.current_window_handle


# browser action9 > All handles
# همه هدل های که باز کردیم را میدهد
# all_handles = driver.window_handles


# browser action10 > switch
# میتوان بین صفحه ها باتوجه به هندل ها switch کرد
# driver.switch_to.window(all_handles[0])

# صفحه را می بندد(در ورژن های جدید خودش می بندد)
# browser action11 > Close Tab
# driver.close()

# browser action12 > quit session
# driver.quit()


# browser action13 > window Size
# window_size = driver.get_window_size()
# window_width_Size = driver.get_window_size()['width']
# window_height_size = driver.get_window_size()['height']

# تعیین  و تغییر سایز پنجره مرورگر
# browser action14 > set window Size
# driver.set_window_size(500, 800)
# size = driver.get_window_size()

#  به دست اوردن موقیعبت پنجره مرورگر
# browser action15 > get window position
# current_window_position = driver.get_window_position()

# تنظیم کردن موقیعت مرورگر
# browser action16 > set window position
# driver.set_window_position(400, 500)

# کمترین مقدار مرورگر
# browser action17 > minimize
# driver.minimize_window()

# بیشترین مقدار پنجره مرورگر
# browser action17 > maximize window
# driver.maximize_window()

# تمام صفحه کردن مرورگر
# browser action17 > full screen window
# driver.fullscreen_window()

# برای استفاده از optionها ی مثل صفحه خصوص باز کردن مرورگر و ...  استفاده می شود
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# باز کردن صفحه خصوصی
# browser action18 > open incognito window
# chrome_options.add_argument("--incognito")

# عملیات بدون باز کردن مرورگر انجام میشود
# browser action19 > dontOpen browser
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(executable_path=r"C:\Program Files\chrom Driver\chromedriver.exe"),
                          options=chrome_options)
