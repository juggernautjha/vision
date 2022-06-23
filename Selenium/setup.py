import os
import wget
import time

user = "rahulj21"
pwd_ = input("Password Batabe: ")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
s = Service('/home/juggernautjha/Rahul/vision/Selenium/chromedriver')
driver = webdriver.Chrome(service = s, options = options)
driver.get('https://hello.iitk.ac.in/user/login')
uname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='name']")))
pwd = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
uname.clear()
pwd.clear()
uname.send_keys(user)
pwd.send_keys(pwd_)
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='edit-submit']")))
log_in.click()
driver.get("https://hello.iitk.ac.in/mth102aa2122/#/home")
listOfElements = driver.find_elements(By.CSS_SELECTOR, "div[class='weekWrapper']")
for i in listOfElements:
    try:
        i.click()
    except:
        pass
