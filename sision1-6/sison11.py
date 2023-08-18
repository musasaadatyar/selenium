from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://material.angular.io/components/input/overview')
driver.implicitly_wait(5)
# 1: get text
# el = driver.find_element(By.XPATH, '//span[@ class="mdc-button__label" and text()= "Components"]').text

# 2: get class
# el1 = driver.find_element(By.XPATH, '//span[@ class="mdc-button__label" and text()= "Components"]').get_attribute('class')

# 3: radio btn & check box
# driver.find_element(By.ID, 'mat-radio-2-input').click()
# el1 = driver.find_element(By.ID, 'mat-radio-2')
# class_el1 = el1.get_attribute('class')
# print(class_el1)
# assert 'checked' not in class_el1
#
# sleep(5)
# el2 = el1.get_attribute('class')
# print(el2)
#
# assert 'checked' in el2;

# 4: switch & check box btn
driver.find_element(By.XPATH, '//span[text()="Ok, Got it"]').click()
sleep(1)
# driver.find_element(By.ID, 'mat-mdc-checkbox-8-input').click()
# toggle = driver.find_element(By.XPATH, '//input[@ id="mat-mdc-checkbox-1-input"]')

# assert 'checked' not in toggle.get_attribute('class')
# toggle.click()
# assert 'checked' in toggle.get_attribute('class')

# get value input
# driver.find_element(By.XPATH, '//input[@id="mat-input-2"]').location_once_scrolled_into_view
# input_element = driver.find_element(By.XPATH, '//input[@id="mat-input-2"]')
# input_element.click()
# driver.find_element(By.XPATH, '//input[@id="mat-input-2"]').send_keys('ksadjahkjh')
# input_value = input_element.get_attribute('value')

# input file error
parent_el = driver.find_element(By.XPATH, "//*[@id ='meta_input_1']")
assert 'dirty' not in parent_el.get_attribute('class')
input_el = driver.find_element(By.ID, 'meta-input-1')
assert 'dirty' in parent_el.get_attribute('class')
