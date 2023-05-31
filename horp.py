import pyautogui
from pynput import keyboard

coordinates = [
    (848, 516),
    (882, 516),
    (919, 518),
    (958, 523),
    (992, 521),
    (1030, 523),
    (1064, 523)
]

previous_colors = {}  # Store the previous color of each pixel
is_pixel_checking = False  # Flag to indicate if pixel checking is active

def check_and_click_pixels():
    for coord in coordinates:
        x, y = coord
        pixel_color = pyautogui.pixel(x, y)

        if coord not in previous_colors:
            previous_colors[coord] = pixel_color
            continue

        previous_color = previous_colors[coord]
        if pixel_color != previous_color:
            pyautogui.click(x, y)
            break  # Stop checking other coordinates after the first click

def on_press(key):
    global is_pixel_checking

    if key == keyboard.Key.space:  # Start/Stop the pixel checking on Space key press
        is_pixel_checking = not is_pixel_checking
        if is_pixel_checking:
            print("Pixel checking started.")
        else:
            print("Pixel checking stopped.")

    if key == keyboard.Key.esc:  # Stop the script on Escape key press
        return False

with keyboard.Listener(on_press=on_press) as listener:
    while listener.running:
        if is_pixel_checking:
            check_and_click_pixels()
