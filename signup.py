from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import re
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ANTI_API_KEY = "2a0d3dd4c7e7c4851b796dc302daa8c1"


def create_undetectable_driver():
    """Create a Chrome driver with anti-detection measures"""

    chrome_options = Options()

    # Essential anti-detection flags
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Additional stealth options
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--allow-running-insecure-content')

    # Randomize user agent
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')

    # Enable performance logging for network monitoring
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    driver = webdriver.Chrome(options=chrome_options)

    # Execute CDP commands to hide automation
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": driver.execute_script("return navigator.userAgent").replace('HeadlessChrome', 'Chrome')
    })

    # Override navigator.webdriver property
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });

            // Mock plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });

            // Mock languages
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });

            // Mock permissions
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications' ?
                    Promise.resolve({ state: Notification.permission }) :
                    originalQuery(parameters)
            );

            // Mock chrome object
            window.chrome = {
                runtime: {}
            };
        '''
    })

    driver.maximize_window()
    return driver


driver = None


def human_like_delay(min_sec=0.5, max_sec=2.0):
    """Add random human-like delays"""
    time.sleep(random.uniform(min_sec, max_sec))


def human_like_type(element, text):
    """Type text with human-like delays between keystrokes"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.15))


def smooth_move_to_element(driver, element):
    """Move mouse to element with smooth human-like path"""
    action = ActionChains(driver)

    # Get element location
    location = element.location
    size = element.size

    # Calculate center of element
    center_x = location['x'] + size['width'] / 2
    center_y = location['y'] + size['height'] / 2

    # Move in steps
    steps = random.randint(10, 20)
    for i in range(steps):
        action.move_by_offset(center_x / steps, center_y / steps)
        action.pause(random.uniform(0.01, 0.03))

    action.perform()


def solve_slider_human_like(slider_element):
    """
    Solve slider with highly human-like behavior
    """
    try:
        print("🤖 Starting human-like slider solve...")

        # Get slider information
        slider_size = slider_element.size
        print(f"📏 Slider width: {slider_size['width']}px")

        # Calculate slide distance (typically 90% of track width)
        # Usually around 260-300px for Alibaba captcha
        slide_distance = random.randint(250, 290)

        action = ActionChains(driver)

        # Move to slider first (human behavior)
        print("👆 Moving mouse to slider...")
        action.move_to_element(slider_element)
        action.pause(random.uniform(0.3, 0.6))
        action.perform()

        human_like_delay(0.5, 1.0)

        # Click and hold
        print("🖱️ Clicking and holding slider...")
        action = ActionChains(driver)
        action.click_and_hold(slider_element)
        action.pause(random.uniform(0.1, 0.3))
        action.perform()

        human_like_delay(0.2, 0.4)

        # Slide with human-like movement pattern
        print("🏃 Sliding...")
        action = ActionChains(driver)

        # Phase 1: Quick initial movement (40% of distance)
        phase1_distance = slide_distance * 0.4
        steps1 = random.randint(8, 12)
        for i in range(steps1):
            offset = phase1_distance / steps1
            y_offset = random.uniform(-1, 1)  # Small vertical wobble
            action.move_by_offset(offset, y_offset)
            action.pause(random.uniform(0.005, 0.015))

        # Phase 2: Slower middle movement (40% of distance)
        phase2_distance = slide_distance * 0.4
        steps2 = random.randint(15, 25)
        for i in range(steps2):
            offset = phase2_distance / steps2
            y_offset = random.uniform(-1.5, 1.5)
            action.move_by_offset(offset, y_offset)
            action.pause(random.uniform(0.015, 0.035))

        # Phase 3: Final adjustment (20% of distance)
        phase3_distance = slide_distance * 0.2
        steps3 = random.randint(5, 10)
        for i in range(steps3):
            offset = phase3_distance / steps3
            y_offset = random.uniform(-0.5, 0.5)
            action.move_by_offset(offset, y_offset)
            action.pause(random.uniform(0.02, 0.05))

        # Small pause before release (human hesitation)
        action.pause(random.uniform(0.1, 0.3))

        # Release
        print("✋ Releasing slider...")
        action.release()
        action.perform()

        print("✅ Slider movement completed")

        # Wait for validation
        time.sleep(3)

        # Check for success
        try:
            # Look for success indicators
            driver.switch_to.default_content()
            time.sleep(1)

            # Check if OTP field appeared (indirect success indicator)
            try:
                otp_field = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'OTP')]")
                print("🎉 SUCCESS! OTP field is now visible!")
                return True
            except:
                pass

            # Check for error message
            try:
                error = driver.find_element(By.XPATH,
                                            "//*[contains(text(), 'unusual traffic') or contains(text(), 'something') and contains(text(), 'wrong')]")
                print("⚠️ Still showing error - captcha may need retry")
                return False
            except:
                pass

            # If no error and no success, uncertain
            print("❓ Status uncertain - please verify manually")
            return None

        except Exception as e:
            print(f"⚠️ Could not verify success: {e}")
            return None

    except Exception as e:
        print(f"❌ Error during slider solve: {e}")
        import traceback
        traceback.print_exc()
        return False


def solve_captcha():
    """Main captcha solving function"""
    try:
        print("\n🎯 Locating slider...")
        human_like_delay(2, 3)

        slider = None
        iframe_index = None

        # Check iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"📦 Found {len(iframes)} iframes")

        for idx, iframe in enumerate(iframes):
            try:
                driver.switch_to.frame(iframe)

                # Try multiple selectors
                selectors = [
                    ".nc_iconfont.btn_slide",
                    ".nc-lang-cnt",
                    "#nc_1_n1z",
                    "[id^='nc_'][id$='_n1z']",
                    ".btn_slide",
                    "[class*='btn_slide']",
                    ".slidetounlock"
                ]

                for selector in selectors:
                    try:
                        slider = driver.find_element(By.CSS_SELECTOR, selector)
                        iframe_index = idx
                        print(f"✅ Found slider in iframe {idx}: {selector}")
                        break
                    except:
                        continue

                if slider:
                    break
                else:
                    driver.switch_to.default_content()

            except Exception as e:
                driver.switch_to.default_content()
                continue

        if not slider:
            print("❌ Could not find slider")
            driver.switch_to.default_content()

            # Check for error/blocked message
            try:
                error_msg = driver.find_element(By.XPATH, "//*[contains(text(), 'unusual traffic')]")
                print("⚠️ DETECTED: Bot detection triggered!")
                print("💡 TIP: Try closing browser completely and running again")
                print("💡 TIP: Or wait a few minutes before retrying")
            except:
                pass

            return False

        # Attempt solve
        result = solve_slider_human_like(slider)

        driver.switch_to.default_content()
        return result

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        driver.switch_to.default_content()
        return False


def signup_test():
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