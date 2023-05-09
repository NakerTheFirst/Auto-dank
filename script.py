import random
import pyautogui
import time

command_delay = {
    "dig": 30,
    "hunt": 30,
    "fish": 30,
    "beg": 40
}


def run_command(text_command, delay):
    pass


big_x = 2300
big_y = 200

small_x = -500
small_y = 850

channel_name = "#dank-memes-bot"  # Replace with the name of your desired channel
dig = "/dig"  # Replace with your desired message
beg = "/beg"
fish = "/fish"
hunt = "/hunt"

# Activate Discord window

# Time to switch to Discord tab
time.sleep(2)
pyautogui.click(x=small_x, y=small_y)  # Replace with the coordinates of the Discord window on your screen
pyautogui.hotkey('ctrl', 'k')  # Open channel search bar
pyautogui.typewrite(channel_name, interval=0.005)  # Type channel name
pyautogui.press('enter', interval=0.1)  # Select channel

# Type message in channel and send
time.sleep(0.2)  # Wait for channel to load
pyautogui.typewrite(dig, interval=0.005)  # Type message
time.sleep(0.05)
pyautogui.press('space', interval=0.1)  # Send message
pyautogui.press('enter', interval=0.1)  # Send message
pyautogui.typewrite(fish, interval=0.1)  # Type message
time.sleep(0.05)
pyautogui.press('space', interval=0.1)  # Send message
pyautogui.press('enter', interval=0.1)  # Send message
pyautogui.typewrite(hunt, interval=0.005)  # Type message
time.sleep(0.05)
pyautogui.press('space', interval=0.1)  # Send message
pyautogui.press('enter', interval=0.1)  # Send message
pyautogui.typewrite(beg, interval=0.005)
time.sleep(0.05)
pyautogui.press('space', interval=0.1)
pyautogui.press('enter', interval=0.1)

# Repeat every 60 seconds
while True:
    random_delay = random.uniform(0.01, 0.015)
    time.sleep(30 + random_delay)

    pyautogui.typewrite(dig, interval=0.005)
    time.sleep(0.05)
    pyautogui.press('space', interval=0.1)
    pyautogui.press('enter', interval=0.1)

    pyautogui.typewrite(fish, interval=0.005)
    time.sleep(0.05)
    pyautogui.press('space', interval=0.1)
    pyautogui.press('enter', interval=0.1)

    pyautogui.typewrite(hunt, interval=0.005)
    time.sleep(0.05)
    pyautogui.press('space', interval=0.1)
    pyautogui.press('enter', interval=0.1)

    time.sleep(10 + random_delay)
    pyautogui.typewrite(beg, interval=0.005)
    time.sleep(0.05)
    pyautogui.press('space', interval=0.1)
    pyautogui.press('enter', interval=0.1)
