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

driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div[2]/a/img').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div[2]/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input').clear()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input').send_keys('3332220000')
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/button').click()
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/img').click()
time.sleep(1)
