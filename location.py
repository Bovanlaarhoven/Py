import pyautogui
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        rgb = pyautogui.pixel(x, y)
        print(f"Clicked at ({x}, {y}) RGB: {rgb}")

# Create a mouse listener
listener = mouse.Listener(on_click=on_click)
listener.start()

# Keep the script running
listener.join()
