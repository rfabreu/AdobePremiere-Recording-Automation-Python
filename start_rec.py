import schedule
import time
from pynput import keyboard


def start_recording():
    with keyboard.Press(keyboard.Key.g):
        keyboard.press(keyboard.Key.g)
        keyboard.release(keyboard.Key.g)


schedule.every().day.at("18:50").do(start_recording)

while True:
    schedule.run_pending()
    time.sleep(1)
