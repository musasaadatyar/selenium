from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from time import sleep

driver = webdriver.Chrome()
driver.get('https://play1.automationcamp.ir/expected_conditions.html')

# 1: sleep
# print(datetime.now())
# sleep(3)
# print(datetime.now())

# 2: implicitly_wait()
# el = driver.implicitly_wait(6)
# try:
#     driver.find_element(By.XPATH, '//*[@name="btnfddddddddddddddddddgdI"]').click()
# except:
#     print('null')

# 3:wait until element has an attribute
# def wait_until_element_has_an_attribute(element_selector, element_locator, attribute, attribute_value, time_out,
#                                         exact=True):
#     for i in range(time_out * 5):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             if exact:
#                 assert element.get_attribute(attribute) == attribute_value
#             else:
#                 assert attribute_value in element.get_attribute(attribute)
#             return
#         except:
#             sleep(0.2)
#     raise Exception('Element attribute is not: ' + str(attribute))
#
# def wait_until_element_not_has_an_attribute(element_selector, element_locator, attribute, attribute_value, time_out,
#                                             exact=True):
#     for i in range(time_out * 5):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             if exact:
#                 assert element.get_attribute(attribute) == attribute_value
#             else:
#                 assert attribute_value not in element.get_attribute(attribute)
#                 print(attribute_value)
#             return
#         except:
#             sleep(0.2)
#     raise Exception('Element attribute is not: ' + str(attribute))

# trigger = driver.find_element(By.ID, 'enabled_trigger')
# trigger.location_once_scrolled_into_view
# trigger.click()
# wait_until_element_not_has_an_attribute(By.ID, 'invisibility_trigger', 'class', 'success', 4, exact=False)
# wait_until_element_has_an_attribute(By.ID, 'invisibility_trigger', 'class', 'danger', 4, exact=False)

# 4: wait until element is enabled
# trigger = driver.find_element(By.ID, 'enabled_trigger')
# trigger.click()
#
# def wait_until_element_is_enabled(element_selector, element_locator,time_out ):
#     for i in range(time_out*2):
#         try:
#             print(++i)
#             element = driver.find_element(element_selector,element_locator)
#             assert element.is_enabled() == True
#             return
#         except:
#             sleep(0.5)
#
# def wait_until_element_is_not_enabled(element_selector, element_locator,time_out ):
#     for i in range(time_out*2):
#         try:
#             print(++i)
#             element = driver.find_element(element_selector,element_locator)
#             assert element.is_enabled() == False
#             return
#         except:
#             sleep(0.5)
#
# wait_until_element_is_enabled(By.ID,'enabled_trigger',3)
# print('element is find')

# 5: wait until element is visible
# def wait_until_element_is_visible(element_selector, element_locator, time_out):
#     for i in range(time_out * 2):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             assert element.is_displayed()
#             print('test not  is passed \n' + str(element.is_displayed()))
#             return
#
#         except:
#             sleep(0.5)
#     raise Exception('element find the ')


# wait until element is invisible
# def wait_until_element_is_invisible(element_selector, element_locator, time_out):
#     for i in range(time_out * 2):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             assert not element.is_displayed()
#             print('test is passed' + str(element.is_displayed()))
#             return
#         except:
#             sleep(0.5)
#     raise Exception('element ont find the  ' )
#
# trigger = driver.find_element(By.ID, 'visibility_trigger')
# trigger.location_once_scrolled_into_view
# trigger.click()
# wait_until_element_is_visible(By.ID, 'visibility_trigger', 4)
# sleep(5)

# 6: webDriver until / until not Expect Conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

trigger = driver.find_element(By.ID, 'enabled_trigger')
trigger.location_once_scrolled_into_view
trigger.click()

# 6-1: element_to_be_clickable
wait = WebDriverWait(driver, 5)
element = wait.until(EC.element_to_be_clickable((By.ID, 'enabled_trigger')))


# 7: wait until page is loaded

def wait_until_page_loaded(time_out):
    for i in range(time_out*2):
        try:
            state = driver.execute_script('return document.readyState')
            assert state == 'complete'
            print(state)
            return
        except:
            sleep(0.5)
wait_until_page_loaded(5)