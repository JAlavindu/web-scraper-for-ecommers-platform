from selenium.webdriver.common.action_chains import ActionChains
import random

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