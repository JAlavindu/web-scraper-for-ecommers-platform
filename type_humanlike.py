import time
import random

def human_like_type(element, text):
    """Type text with human-like delays between keystrokes"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.15))