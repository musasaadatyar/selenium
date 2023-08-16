from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# service = Service(executable=r'C:\Program Files\chromDriver\chromedriver.exe')
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.maximize_window()
driver.get('https://trytestingthis.netlify.app')

# doubleClick
# element_double_click = driver.find_element('xpath', "//button[text()='Double-click me']")
# actions.double_click(element_double_click).perform()
# driver.find_element('xpath', "//p[text()='Your Sample Double Click worked!']")

# right click
# el = driver.find_element('id', 'fname')
# actions.context_click(el).perform()

# hover mouse or move mouse
# el = driver.find_element('class name', 'tooltip')
# actions.move_to_element(el).perform()

# driver.get('https://demos.telerik.com/kendo-ui/circular-gauge/index')
driver.implicitly_wait(6)

# driver.find_element('id', 'onetrust-accept-btn-handler').click()
# driver.execute_script('scroll(0,200)')

# click and hold click
# el2 = driver.find_element('xpath', '// a[@title="Increase"]')
# actions.click_and_hold(el2).perform()
# actions.release(el2)

# puse and release
# el1 = driver.find_element('xpath', '// a[@title="Decrease"]')
# el2 = driver.find_element('xpath', '// a[@title="Increase"]')
# actions.click_and_hold(el1).pause(4).release().click_and_hold(el2).pause(3).perform()

# drag and drop
# driver.get('https://www.javatpoint.com/html-drag-and-drop')
# driver.implicitly_wait(10)

# el1 = driver.find_element('xpath', "//img[@id='drag1']")
# el2 = driver.find_element('xpath', "//img[@id='div1']")

# actions.move_to_element(el1).click_and_hold().move_to_element(el2).release().perform()
# actions.drag_and_drop(el1,el2).perform()

# get cordinate
offset = driver.find_element('xpath', '//*[text()="Lets you select multiple options"]').location
# مختصات را می دهد
print(offset)
#  click out of the element there was no element
# driver.find_element('id','option').click()
# actions.move_by_offset(offset['x'],offset['y']).pause(6).click().perform()


# drag and drop by offset
# el1 = driver.find_element('xpath', "//img[@id='drag1']")
# cor_el1 = driver.find_element('xpath', "//img[@id='div1']").location
# cor_el2= driver.find_element('xpath', "//img[@id='div1']").location
# offset_x = cor_el1['x'] - cor_el2['x']
# offset_y = cor_el1['y'] - cor_el2['y']

# actions.drag_and_drop_by_offset(el1,el2.offset_x, offset_y).perform()
sleep(3)
