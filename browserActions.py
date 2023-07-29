# # برای این که درایور مربوط به هر کروم را دانلود کند از این کد استفاده می کنیم
from selenium import webdriver

#برای ادرس دادن در selenium v4
from selenium.webdriver.chrome.service import Service as ChromeService

# برای  دانلود کردن درایور مربوط به مرورگر اگر فیلتر نباشد
from webdriver_manager.chrome import ChromeDriverManager

# کمتر از sleep استفاده شود
from time import sleep
# auto install chromDriver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# selenium v4
driver = webdriver.Chrome(service=ChromeService(executable_path=r"C:\Program Files\chrom Driver\chromedriver.exe"))
# driver = webdriver.Chrome( executable_path=r"C:\Program Files\chrom Driver\chromedriver.exe")

# browser action1 > open web
driver.get('https://www.google.com/')
# sleep(2)

# browser action2 > title page
# window_title = driver.title
# print(window_title)

# browser action3 > back page
# driver.get("https://www.wikipedia.org/")
# sleep(3)

# back to the last page
# driver.back()
# sleep(2)

# browser action4 > forward
# انتقال دوباره از صفحه back به جلو
# driver.forward()

# browser action5 > refresh
# driver.refresh()
# print('refresh')

#open new windows
# browser action6 > open new window and switch to it(tab)
# driver.switch_to.new_window('tab')
# print(driver.title)
# sleep(3)

# browser action7 > open new window and switch to it( window)
# driver.switch_to.new_window('window')
# driver.get('https://labtob.ir/')
# sleep(2)

# browser action8 > Current window
# labtobWindow = driver.current_window_handle
# print('labtobWindow: ' + str(labtobWindow))

# browser action9 > All handles
# all_handles = driver.window_handles
# print('all_handle: ' + str(all_handles))

# browser action10 > switch
# driver.switch_to.window(all_handles[0])

# browser action11 > Close Tab
# driver.close()

# browser action12 > quit session
# driver.quit()

# browser action13 > window Size
# window_size = driver.get_window_size()
# window_width_Size = driver.get_window_size()['width']
# window_height_size = driver.get_window_size()['height']
# print(window_height_size)

# browser action14 > set window Size
# driver.set_window_size(500, 800)
# size = driver.get_window_size()
# sleep(3)
# assert size['width'] == 800

# browser action15 > get window position
# current_window_position = driver.get_window_position()
# print(current_window_position)

# browser action16 > set window position
# driver.set_window_position(400, 500)
# assert driver.get_window_position()['x'] == 400;

# browser action17 > minimize
# driver.minimize_window()
# sleep(3)

# browser action17 > maximize window
# driver.maximize_window()
# sleep(2)

# browser action17 > full screen window
# driver.fullscreen_window()
# sleep(6)

