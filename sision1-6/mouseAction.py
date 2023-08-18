from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# service = Service(executable=r'C:\Program Files\chromDriver\chromedriver.exe')
# driver = webdriver.Chrome(service=Service(executable_path=r'C:\Program Files\chromDriver\chromedriver.exe'))
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.maximize_window()

driver.get('https://trytestingthis.netlify.app')
driver.implicitly_wait(5);


# 1:doubleClick
# element_double_click = driver.find_element('xpath', "//button[text()='Double-click me']")
# actions.double_click(element_double_click).perform()
# driver.find_element('xpath', "//p[text()='Your Sample Double Click worked!']")

# 2:right click
# el = driver.find_element('id', 'fname')
# actions.context_click(el).perform()

# 3:hover mouse or move mouse
# el = driver.find_element('class name', 'tooltip')
# actions.move_to_element(el).perform()

# driver.get('https://demos.telerik.com/kendo-ui/circular-gauge/index')
# driver.implicitly_wait(6)

# driver.find_element('id', 'onetrust-accept-btn-handler').click()
# driver.execute_script('scroll(0,200)')

# 4:click and hold click
# el2 = driver.find_element('xpath', '// a[@title="Increase"]')
# actions.click_and_hold(el2).perform()
# actions.release(el2)

# 5:pause and release
# el1 = driver.find_element('xpath', '// a[@title="Decrease"]')
# el2 = driver.find_element('xpath', '// a[@title="Increase"]')
# actions.click_and_hold(el1).pause(4).release().click_and_hold(el2).pause(3).perform()

# 6:drag and drop
# driver.get('https://www.javatpoint.com/html-drag-and-drop')
# driver.implicitly_wait(10)

# el1 = driver.find_element('xpath', "//img[@id='drag1']")
# el2 = driver.find_element('xpath', "//img[@id='div1']")

# actions.move_to_element(el1).click_and_hold().move_to_element(el2).release().perform()
# actions.drag_and_drop(el1,el2).perform()

# 7:get coordinate
# offset = driver.find_element('xpath', '//*[text()="Lets you select multiple options"]').location
# مختصات را می دهد

#  8:click out of the element there was no element
# driver.find_element('id','option').click()
# actions.move_by_offset(offset['x'],offset['y']).pause(6).click().perform()


# 9:drag and drop by offset center
# el1 = driver.find_element('xpath', "//img[@id='drag1']")
# el2 = driver.find_element('xpath', "//img[@id='drag2']")
# cor_el1 = driver.find_element('xpath', "//img[@id='div1']").location
# cor_el2= driver.find_element('xpath', "//img[@id='div1']").location
# offset_x = (cor_el1['x'] - cor_el2['x']) + (el2.rect['width']-el2.rect['width']) /2
# offset_y = (cor_el1['y'] - cor_el2['y']) + (el2.rect['height']-el2.rect['height'])/2

# actions.drag_and_drop_by_offset(el1,el2.offset_x, offset_y).perform()

# driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
# driver.implicitly_wait(6)


# ====> session10 - scroll in browser
# 10: scroll commend with js

# 1: scrollBy  => صفحه هر جای باشد  اسکرول میخورد
# driver.execute_script("window.scrollBy(0,600)")

# 2: scrollTo  => صفحه فقط در این مقدار میرود و اگر در این مقدار باشد دیگر ثابت می ماند
# driver.execute_script("window.scrollTo(0,600)")
# el = driver.find_element('xpath', '//h3[text()="48. The Intouchables"]')
# driver.execute_script('arguments[0].scrollIntoView()', el)

# 3: scroll when there was no item


# 4:scroll element if curently cannot be found or not sure if it is in the page(assertion)
# def scroll_to_find_element(location, pixel):
#     for i in range(10):
#         try:
#             driver.find_element(location[0], location[1])
#             return f"the element locate has be {location[1]} found"
#         except:
#             driver.execute_script(
#                 f"window.scrollTo(0,{str(pixel)})"
#             )
#             sleep(0.5)
#     raise Exception(f'the locate{location[1]} element not find')

# 4:scroll element if curently cannot be found or not sure if it is in the page(true-false)
# def scroll_to_find_element(location, pixel):
#     for i in range(10):
#         try:
#             driver.find_element(location[0], location[1])
#             return True
#         except:
#             driver.execute_script(
#                 f"window.scrollTo(0,{str(pixel)})"
#             )
#             sleep(0.5)
#     return False

# driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
# driver.implicitly_wait(10)

# 5:scroll to down of the page
# driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')

# 6:scroll to up of the page
# driver.execute_script('window.scrollBy(0,0)')

# 7: scroll horizontal
# driver.execute_script("document.querySelector('table td:last-child').scrollIntoView()")

# 8: scroll use actionChains
# el1 = driver.find_element('xpath',"//button[text()=' Submit']")
# el2 = driver.find_element('id','fname')
# actions.move_to_element(el2).pause(3).move_to_element(el1).pause(4).perform()

# 9 scroll use keyboard
# el = driver.find_element('tag name', 'html')
# actions.send_keys_to_element(el, Keys.END).perform()
# actions.send_keys_to_element(el, Keys.UP).perform()


# page_elemnt = driver.find_element('tag name', 'html')
# def scroll_to_find_element(locator):
#     for i in range(10):
#         try:
#             driver.find_element(locator[0], locator[1])
#         except:
#             actions.send_keys_to_element(page_elemnt, Keys.PAGE_DOWN).perform()
#             sleep(0.5)
#     return False
# result = scroll_to_find_element(['id', 'demdsfsfso'])

# scroll to the element we find
# element = driver.find_element('xpath', '//h4[text()=" Please suggest any improvements to this website. You can reach me in "]')
# element.location_once_scrolled_into_view

# scroll horizentall
# element = driver.find_element('xpath', '//h4[text()=" Please suggest any improvements to this website. You can reach me in "]')
# element.location_once_scrolled_into_view

sleep(5)

