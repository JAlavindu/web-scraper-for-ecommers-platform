from selenium import webdriver


driver = webdriver.Chrome()

def daraz_open():

    driver.get("https://www.daraz.lk/#?")
    driver.maximize_window()
