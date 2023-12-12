import pyautogui
import time
import os
from PIL import Image
from skimage import io
import numpy as np

# get the size of the primary monitor
screen_width, screen_height = pyautogui.size()

# specify folder where the screenshots are saved
upload_folder = "./static/screenshots"

game_on = True
# set screenshot size in pixels
sc_x = 140
sc_y = 30


# pyautogui.moveTo(100, 150)

cactus_x = 430
cactus_y = 640

def take_screenshot():
    """Takes screenshot of small area and returns it as NumPy array"""
    jump_region = pyautogui.screenshot(region=(cactus_x, cactus_y, sc_x, sc_y))

    # Convert PIL.Image.Image to NumPy array
    jump_region_np = np.array(jump_region)
    return jump_region_np

def get_rgb_avg(jump_region_np):
    mean_color = jump_region_np.mean(axis=0).mean(axis=0)
    px_sum = sum(mean_color)
    return px_sum

while game_on:
    jump_region_np = take_screenshot()
    avg_color = get_rgb_avg(jump_region_np)

    if avg_color < 765:
        pyautogui.press("space")

    time.sleep(0.1                        )

