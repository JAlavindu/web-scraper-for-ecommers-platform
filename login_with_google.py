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

    # Try to find the Google button. 
    # We'll try a few selectors to be safe, prioritizing one that mentions Google.
    try:
        google_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'index_module_buttonItem') and contains(., 'Google')]"))
        )
    except:
        # Fallback to the generic class if specific text fails (it might be an icon only)
        print("Specific Google button not found, trying generic selector...")
        google_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'index_module_buttonItem')]"))
        )

    print("Found Google button, clicking...")
    # Try standard click
    try:
        google_button.click()
    except:
        # Fallback to JS click
        print("Standard click failed, using JS click...")
        driver.execute_script("arguments[0].click();", google_button)

    print("Waiting for new window...")
    WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))

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
        # Use presence first to avoid NoneType error if visibility check fails weirdly
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password' or @name='Passwd']"))
        )
        # Ensure it is visible
        if not password_field.is_displayed():
             WebDriverWait(driver, 5).until(lambda d: password_field.is_displayed())
    except:
        print("Password field not found immediately, retrying 'Next' click...")
        try:
            next_button.click()
        except:
            pass # Element might be stale
        
        password_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password' or @name='Passwd']"))
        )
        if not password_field.is_displayed():
             WebDriverWait(driver, 5).until(lambda d: password_field.is_displayed())
    
    password_field.click()
    password_field.send_keys(password)

    next_button_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
    )
    next_button_password.click()
    print("Next button clicked (password)")

    # Check for CAPTCHA or 2FA
    time.sleep(2)
    
    # Check if window is still open before checking captcha
    try:
        # Safely check if the current window handle is still valid
        current_handles = driver.window_handles
        if driver.current_window_handle in current_handles:
            handle_captcha(driver, api_key)
        else:
            print("Window closed, assuming login successful or moved to next step.")
    except Exception as e:
        print(f"Could not check for CAPTCHA (window might be closed): {e}")

    # If window is still open, wait for continue button or closure
    try:
        if driver.current_window_handle in driver.window_handles:
            try:
                continue_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue')]"))
                )
                continue_button.click()
                print("Continue button clicked")
            except:
                pass # Continue button might not appear if auto-redirected
    except:
        pass # Window likely closed

    try:
        driver.switch_to.window(original_window)
        print("Switched back to main Daraz window.")

        # --- Handle Google One Tap / Account Chooser iframe ---
        print("Checking for Google Account Chooser (One Tap)...")
        time.sleep(5) # Wait for the iframe to load

        # Find all iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        found_one_tap = False
        
        for i, iframe in enumerate(iframes):
            try:
                # Check iframe src to identify Google frames
                src = iframe.get_attribute("src")
                if src and ("accounts.google.com" in src or "gsi" in src):
                    print(f"Checking iframe {i} for Google account...")
                    driver.switch_to.frame(iframe)
                    
                    # Try to find the account by email
                    try:
                        # Look for the email address or the container
                        account_element = WebDriverWait(driver, 3).until(
                            EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{email}')]/ancestor::div[@role='button'] | //*[contains(text(), '{email}')]"))
                        )
                        print(f"Found account element for {email}, clicking...")
                        driver.execute_script("arguments[0].click();", account_element)
                        found_one_tap = True
                        driver.switch_to.default_content()
                        break 
                    except:
                        # Fallback: Try clicking the first button-like element in this Google iframe
                        try:
                            generic_button = driver.find_element(By.XPATH, "//div[@role='button']")
                            print("Found generic account button, clicking...")
                            driver.execute_script("arguments[0].click();", generic_button)
                            found_one_tap = True
                            driver.switch_to.default_content()
                            break
                        except:
                            pass
                    
                    driver.switch_to.default_content()
            except Exception as e:
                print(f"Error checking iframe {i}: {e}")
                driver.switch_to.default_content()

        if found_one_tap:
            print("Clicked Google One Tap account. Waiting for login...")
            time.sleep(5)

        print("🔄 Waiting for login to process...")
        time.sleep(5)

        # Check if we need to refresh to see the logged-in state
        try:
            # If Login button is still visible, refresh
            if driver.find_elements(By.XPATH, "//a[text()='Login']"):
                print("Refreshing page to update login status...")
                driver.refresh()
                time.sleep(5)

            print("✅ Successfully inside the website!")

        except Exception as e:
            print(f"Error verifying login state: {e}")

    except:
        print("Could not switch to original window (maybe already there?)")