from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import time
from selenium import webdriver
recipient_email = sys.argv[1]
message = sys.argv[2]
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)


s = Service("C:/Users/patha/OneDrive/Desktop/chromedriver.exe")

driver.get('http://www.google.com')
time.sleep(2)

user_input = driver.find_element(By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys('https://www.gmail.com')
time.sleep(2)
user_input.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH,value='//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3').click()
time.sleep(2)
# #
user_input2 = driver.find_element(By.XPATH , value = '/html/body/header/div/div/div/a[2]').click()
time.sleep(2)

# user_input2.send_keys(Keys.ENTER)
user_input3 = driver.find_element(By.XPATH,value='//*[@id="identifierId"]')
time.sleep(2)
user_input3.send_keys('webscrapper7896@gmail.com')
driver.find_element(By.XPATH , value = '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(2)
user_input4 = driver.find_element(By.XPATH,value='//*[@id="password"]/div[1]/div/div[1]/input')
time.sleep(2)
user_input4.send_keys('7744050941')
driver.find_element(By.XPATH, value='//*[@id="passwordNext"]/div/button/span').click()
time.sleep(2)
driver.find_element(By.XPATH, value='/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div').click()
time.sleep(2)
user_input5 = driver.find_element(By.XPATH, value='//*[@id=":bp"]')
time.sleep(2)
user_input5.send_keys(recipient_email)
time.sleep(2)
user_input6 = driver.find_element(By.XPATH, value='//*[@id=":9d"]')
time.sleep(2)
user_input6.send_keys(message)
driver.find_element(By.XPATH, value='//*[@id=":7s"]').click()
# link2.click()
# old_height = driver.execute_script('return document.body.scrollHeight')
# while True:
#     try:
#         driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
#         time.sleep(2)
#
#         new_height = driver.execute_script('return document.body.scrollHeight')
#         print(old_height)
#         print(new_height)
#         if new_height == old_height:
#             break
#         old_height = new_height
#     except:
#         print('nothing to load')
# html = driver.page_source
# with open('smartprix.html','w',encoding='utf-8') as f:
# f.write(html)