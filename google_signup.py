from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enter_password_email import password_email

import open_daraz

def signup_with_google(driver):
    print("Signing up with Google account...")
    check_box = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'iweb-checkbox-icon')]"))
    )
    check_box.click()
    print("checkbox clicked")
    google_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'index_module_buttonItem')]")
        )
    )

    print(google_button.is_displayed())
    google_button.click()

    print("Google sign-up button clicked!")

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    new_window = [w for w in driver.window_handles if w != driver.current_window_handle][0]
    driver.switch_to.window(new_window)
    print("Switched to Google login window")

    # --- Now wait for the email input field ---
    email, password = password_email()

    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_field.send_keys(email)

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'VfPpkd-RLmnJb')]"))
    )
    next_button.click()
    print("Next button clicked (email)")

    # Wait for password input field
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Passwd"))
    )
    password_field.send_keys(password)

    next_button_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'VfPpkd-RLmnJb')]"))
    )
    next_button_password.click()
    print("Next button clicked (password)")