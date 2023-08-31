import pyautogui
import time
import random

def hold_key(key, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.keyDown(key)
        time.sleep(0.01)

if __name__ == "__main__":
    print("Press 'Ctrl+C' to exit the script.")
    while True:
        if pyautogui.keyDown('ctrl') and pyautogui.press('c'):
            print("Exiting the script.")
            break
        
        time.sleep(1)

        random_duration = random.uniform(25, 27)
        pyautogui.mouseDown(button='left')
        
        hold_key('d', random_duration)
        hold_key('a', random_duration)
        hold_key('d', random_duration)
        hold_key('a', random_duration)
        hold_key('d', random_duration)
        
        pyautogui.mouseUp(button='left')
