from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()


def signup_test():


    driver.get("https://www.daraz.lk/#?")
    signUpButton = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
    print(signUpButton.is_displayed())
    signUpButton.click()

    input_phone_num()
    try:
        checkbox = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,
                                       "//div[contains(@class,'iweb-dialog-container-enter')]//div[contains(@class,'iweb-button-mask')]"))
                                                   )
        checkbox.click()
        print("chekbox clicked")
    except Exception as e:
        print(f"checkbox was not clickable: {e}")


    time.sleep(2)

    try:
        otp_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                       "//div[contains(@class,'iweb-dialog-container-enter')]//button[normalize-space()='Send OTP']"))
                                                   )
        otp_button.click()
        print("OTP button clicked")
    except Exception as e:
        print(f"OTP button was not clickable: {e}")
        driver.quit()
        return

    # try:
    #     otp_input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
    #                                    "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter the OTP']"))
    #                                                )
    #     print("OTP input field is present")
    # except Exception as e:
    #     print(f"OTP input field not found: {e}")
    #     driver.quit()
    #     return

    time.sleep(5)
    driver.quit()

def input_phone_num():
    phone_num = input("Enter your phone number: ")
    phone_input = driver.find_element(By.XPATH, "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter your phone number']")
    phone_input.send_keys(phone_num)

def input_otp():
    otp = input("Enter the OTP sent to your phone: ")
    otp_input = driver.find_element(By.XPATH, "//div[contains(@class,'iweb-dialog-container-enter')]//input[@placeholder='Please enter the OTP']")
    otp_input.send_keys(otp)


