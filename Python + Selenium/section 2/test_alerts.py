from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link="http://suninjuly.github.io/alert_accept.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    button=browser.find_element(By.TAG_NAME, "button")
    button.click()
    confirm=browser.switch_to.alert
    confirm.accept()
    x=int(browser.find_element(By.ID, 'input_value').text)
    inpt=browser.find_element(By.ID, "answer")
    inpt.send_keys(str(math.log(abs(12*math.sin(x)))))
    button=browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(7)
finally:
    browser.quit()