import pyautogui
import time

def hold_key(key, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.keyDown(key)

if __name__ == "__main__":
    print("Press 'Ctrl+C' to exit the script.")
    while True:
        if pyautogui.keyDown('ctrl') and pyautogui.press('c'):
            print("Exiting the script.")
            break

        hold_key('d', 250)
        hold_key('a', 250)
