import pyautogui
import time

COMMANDS = {
    "/dig": 30,
    "/hunt": 30,
    "/fish": 30,
    "/beg": 40
}

DISCORD_WINDOW_COORDINATES = {
    "big": (2300, 200),
    "small": (-500, 850)
}

CHANNEL_NAME = "#dank-memes-bot"


def enter():
    pyautogui.press('enter', interval=0.25)
    pyautogui.press('enter', interval=0.3)


def switch_to_discord_tab():
    time.sleep(2)
    pyautogui.click(x=DISCORD_WINDOW_COORDINATES["small"][0], y=DISCORD_WINDOW_COORDINATES["small"][1])


def type_channel_name(channel_name):
    pyautogui.hotkey('ctrl', 'k')
    pyautogui.typewrite(channel_name, interval=0.005)
    pyautogui.press('enter', interval=0.1)
    time.sleep(0.2)


def send_message(message):
    pyautogui.typewrite(message, interval=0.05)
    time.sleep(0.25)
    enter()


def send_commands():
    switch_to_discord_tab()
    time.sleep(0.35)
    type_channel_name(CHANNEL_NAME)

    for command in COMMANDS:
        send_message(command)
        time.sleep(0.35)


def run_commands():
    while True:
        time.sleep(10)

        for command in COMMANDS:
            pyautogui.typewrite(command, interval=0.05)
            enter()
            time.sleep(0.35)


send_commands()
run_commands()
