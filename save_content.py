import schedule
import time
from pynput import keyboard


def save_content():
    with keyboard.Press(keyboard.Key.enter):
        keyboard.press(keyboard.Key.enter)
        keyboard.release(keyboard.Key.enter)


schedule.every().day.at("20:48").do(save_content)

while True:
    schedule.run_pending()
    time.sleep(1)
