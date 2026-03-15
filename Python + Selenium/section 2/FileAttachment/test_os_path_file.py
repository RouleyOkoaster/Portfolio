from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link="http://suninjuly.github.io/file_input.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    frst_name=browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    frst_name.send_keys("Word")
    lst_name=browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lst_name.send_keys("Word")
    mail=browser.find_element(By.CSS_SELECTOR, "[name='email']")
    mail.send_keys("Word")
    current_dir=os.path.abspath(os.path.dirname(__file__))
    file_path=os.path.join(current_dir, "file.txt")
    attach=browser.find_element(By.CSS_SELECTOR, "[type='file']")
    attach.send_keys(file_path)
    button=browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(7)
finally:
    browser.quit()
    