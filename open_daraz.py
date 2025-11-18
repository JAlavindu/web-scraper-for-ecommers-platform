from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

def daraz_open():

    driver.get("https://www.daraz.lk/#?")
    driver.maximize_window()
