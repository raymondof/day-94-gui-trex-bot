import pyautogui
import time
import numpy as np

# get the size of the primary monitor
screen_width, screen_height = pyautogui.size()

# specify folder where the screenshots are saved
upload_folder = "./static/screenshots"

# while True:
#     # get the XY position of the mouse
#     current_mouse_x, current_mouse_y = pyautogui.position()
#     print(current_mouse_x, current_mouse_y)
#     time.sleep(1)
#     pyautogui.press("space")

# INTEGRATED GAME VALUES
# sc_x = 70
# sc_y = 5
#
# cactus_x = 780
# cactus_y = 250

# FULL SCREEN GAME VALUES
# set screenshot size in pixels
cactus_x = 430
cactus_y = 640

# set screenshot size in pixels
sc_x = 160
sc_y = 30

game_on = True


def take_screenshot():
    """Takes screenshot of small area and returns it as NumPy array"""
    jump_region = pyautogui.screenshot(region=(cactus_x, cactus_y, sc_x, sc_y))

    # Convert PIL.Image.Image to NumPy array
    jump_np = np.array(jump_region)
    return jump_np


def get_rgb_avg(img_region_np):
    """Takes NumPy array as an input and calculates the average color of each RGB channel
    and takes sum of them. The background of the game is white 255, 255, 255. Therefore,
    they sum 765."""
    mean_color = img_region_np.mean(axis=0).mean(axis=0)
    px_sum = sum(mean_color)
    return px_sum


while game_on:
    jump_region_np = take_screenshot()
    avg_color = get_rgb_avg(jump_region_np)

    if avg_color < 763:
        pyautogui.press("space")

    time.sleep(0.1)
