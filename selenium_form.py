# Open https://the-internet.herokuapp.com/login

# Please automate next test cases:
# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element_by_css_selector('#username').send_keys('tomsmith')
driver.find_element_by_css_selector('#password').send_keys('SuperSecretPassword!')
driver.find_element_by_css_selector(('.radius')).click()
element = driver.find_element_by_css_selector('.flash.success')
assert element.text == 'You logged into a secure area!\n×'
driver.quit()

# 2. Login with invalid creds and check validation error

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element_by_css_selector('#username').send_keys('tomsmit')
driver.find_element_by_css_selector('#password').send_keys('SuperSecretPassword!')
driver.find_element_by_css_selector(('.radius')).click()
element = driver.find_element_by_css_selector('.flash.error')
assert element.text == 'Your username is invalid!\n×'
driver.quit()

# 3. Logout from app and assert you successfully logged out

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element_by_css_selector('#username').send_keys('tomsmith')
driver.find_element_by_css_selector('#password').send_keys('SuperSecretPassword!')
driver.find_element_by_css_selector(('.radius')).click()
driver.find_element_by_css_selector(('.button.secondary.radius')).click()
element = driver.find_element_by_css_selector('.flash.success')
assert element.text == 'You logged out of the secure area!\n×'
driver.quit()
