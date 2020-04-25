"""Automated Amazon Balance Checker"""

import os
import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

AMAZON_USERNAME = ""
AMAZON_PASSWORD = ""

driver = webdriver.Firefox(executable_path="D:\geckodriver.exe")
wait = WebDriverWait(driver, 10)
    
def signIn():
    
    driver.get('https://www.amazon.in/ap/signin/')
    print("Opening Amazon.in")
    wait.until(EC.title_is('Amazon Business Sign In'))
    driver.find_element_by_id('ap_email').send_keys(AMAZON_USERNAME)
    driver.find_element_by_id('ap_password').send_keys(AMAZON_PASSWORD)
    print("Entered Credentials")
    driver.find_element_by_id('signInSubmit').click()
    print("Signed In")

signIn()


def checkBalance():
    driver.get("https://www.amazon.in/gp/sva/dashboard?ref_=nav_cs_apay")
    print("Opening AmazonPay Balance Page")
    time.sleep(2)
    print("Just Hold for 2 Seconds")
    balance = driver.find_element_by_class_name("currency-green").text
    print("Avaialable Amazon Pay Balance is",balance)
    
checkBalance()