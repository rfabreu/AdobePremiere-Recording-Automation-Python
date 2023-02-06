import schedule
import time
from pynput import keyboard


def stop_recording():
    with keyboard.Press(keyboard.Key.esc):
        keyboard.press(keyboard.Key.esc)
        keyboard.release(keyboard.Key.esc)


schedule.every().day.at("20:45").do(stop_recording)

while True:
    schedule.run_pending()
    time.sleep(1)
