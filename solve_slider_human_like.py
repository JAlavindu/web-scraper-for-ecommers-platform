from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
import human_like_delay

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