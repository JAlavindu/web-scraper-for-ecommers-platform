import time
import random

def human_like_delay(min_sec=0.5, max_sec=2.0):
    """Add random human-like delays"""
    time.sleep(random.uniform(min_sec, max_sec))