from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from delay_humanlike import human_like_delay
from captcha_solve import solve_captcha
from undetectable_driver import create_undetectable_driver
from smooth_movement import smooth_move_to_element
from type_humanlike import human_like_type

def accessing_daraz():
    global driver

    try:
        print("🚀 Creating undetectable browser session...")
        driver = create_undetectable_driver()

        print("🌐 Loading Daraz homepage...")
        driver.get("https://www.daraz.lk/#?")
        human_like_delay(2, 3)

        # Scroll a bit (human behavior)
        driver.execute_script("window.scrollTo(0, 300);")
        human_like_delay(1, 2)
        driver.execute_script("window.scrollTo(0, 0);")
        human_like_delay(0.5, 1)

        # Click Sign Up
        print("📝 Clicking Sign Up...")
        signUpButton = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
        smooth_move_to_element(driver, signUpButton)
        human_like_delay(0.3, 0.7)
        signUpButton.click()
        human_like_delay(2, 3)

        # Input phone number
        phone_num = input("📱 Enter your phone number: ")
        phone_input = driver.find_element(
            By.XPATH,
            "//input[@placeholder='Please enter your phone number']"
        )

        # Click on input field first
        phone_input.click()
        human_like_delay(0.3, 0.6)

        # Type with human-like delays
        print("⌨️ Typing phone number...")
        human_like_type(phone_input, phone_num)
        print(f"✅ Entered phone: {phone_num}")
        human_like_delay(1, 2)

        # Click checkbox
        try:
            print("☑️ Clicking checkbox...")
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'iweb-checkbox-icon')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            human_like_delay(0.5, 1)

            # Use JavaScript click to avoid detection
            driver.execute_script("arguments[0].click();", checkbox)
            print("✅ Checkbox clicked")
        except Exception as e:
            print(f"❌ Checkbox error: {e}")

        human_like_delay(1.5, 2.5)

        # Click OTP button
        try:
            print("🚀 Clicking OTP button...")
            otp_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'index_module_otpText')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", otp_button)
            human_like_delay(0.5, 1)
            driver.execute_script("arguments[0].click();", otp_button)
            print("✅ OTP button clicked")
        except Exception as e:
            print(f"❌ OTP button error: {e}")
            return

        # Wait for captcha
        print("\n⏳ Waiting for captcha to load...")
        time.sleep(5)

        print("\n" + "=" * 70)
        print("SOLVING CAPTCHA")
        print("=" * 70)

        # Attempt to solve
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            print(f"\n🔄 Attempt {attempt}/{max_attempts}")

            result = solve_captcha()

            if result is True:
                print("\n🎉 Captcha solved successfully!")
                break
            elif result is False:
                if attempt < max_attempts:
                    print(f"⚠️ Failed, retrying in 3 seconds...")
                    time.sleep(3)
                else:
                    print("\n❌ All attempts failed")
                    print("\n💡 MANUAL INTERVENTION NEEDED")
                    print("Please solve the captcha manually and press Enter...")
                    input()
            else:
                print("\n❓ Uncertain result")
                print("Did the captcha solve? (y/n): ", end='')
                if input().lower() == 'y':
                    result = True
                    break

        if result:
            # Wait for OTP to arrive
            print("\n✅ Waiting for OTP to be sent...")
            time.sleep(3)

            # Input OTP
            try:
                otp = input("🔐 Enter the OTP sent to your phone: ")
                otp_input = driver.find_element(
                    By.XPATH,
                    "//input[contains(@placeholder, 'OTP')]"
                )
                human_like_type(otp_input, otp)
                print(f"✅ Entered OTP")

                human_like_delay(1, 2)

                # Submit
                try:
                    submit_btn = driver.find_element(By.XPATH,
                                                     "//button[contains(text(), 'Verify') or contains(text(), 'Submit')]")
                    submit_btn.click()
                    print("✅ Submitted!")
                except:
                    print("⚠️ Couldn't find submit button - press manually")

                print("\n🎉 SIGNUP PROCESS COMPLETED!")

            except Exception as e:
                print(f"❌ Error with OTP: {e}")

        print("\n📌 Press Enter to close...")
        input()

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if driver:
            driver.quit()