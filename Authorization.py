import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
#Open site
driver.get("https://qa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '.fieldset:nth-child(1) input').send_keys('da.markushin@gmail.com')
driver.find_element(By.CSS_SELECTOR, '.fieldset:nth-child(2) input').send_keys('12345678')
driver.find_element(By.CSS_SELECTOR, '.btn').click()
time.sleep(5)