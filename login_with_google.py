from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from enter_password_email import password_email
import time
from captcha_utils import handle_captcha

def google_login(driver, api_key=None):
    print("logging in with Google account...")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']")))
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'iweb-dialog')]")))

    google_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'index_module_buttonItem')]")
    ))
    google_button.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    original_window = driver.current_window_handle

    new_window = [w for w in driver.window_handles if w != driver.current_window_handle][0]
    driver.switch_to.window(new_window)
    driver.maximize_window()
    print("Switched to Google login window")

    # --- Now wait for the email input field ---
    email, password = password_email()

    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_field.send_keys(email)

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
    )
    next_button.click()
    print("Next button clicked (email)")

    # Check for CAPTCHA
    time.sleep(2)
    handle_captcha(driver, api_key)

    # Wait for password input field
    time.sleep(3)
    try:
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password' or @name='Passwd']"))
        )
    except:
        print("Password field not found immediately, retrying 'Next' click...")
        try:
            next_button.click()
        except:
            pass # Element might be stale
        password_field = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password' or @name='Passwd']"))
        )
    
    password_field.click()
    password_field.send_keys(password)

    next_button_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
    )
    next_button_password.click()
    print("Next button clicked (password)")

    # Check for CAPTCHA or 2FA
    time.sleep(2)
    handle_captcha(driver, api_key)

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue')]"))
    )
    continue_button.click()
    print("Continue button clicked")

    driver.close()  # close Google popup
    driver.switch_to.window(original_window)
    print("Switched back to main Daraz window.")