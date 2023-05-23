import pyautogui
from pynput import keyboard

# Function to check if a pixel is white
def is_pixel_white(x, y):
    pixel_color = pyautogui.pixel(x, y)
    # Assuming white pixels have RGB values (255, 255, 255)
    return pixel_color == (255, 255, 255)

# Function to simulate a human-like click
def human_like_click(x, y):
    # Move the cursor near the target location
    pyautogui.moveTo(x + 5, y + 5, duration=0.5)

    # Click at the target location
    pyautogui.click(x, y)
    print(f"Clicked at pixel ({x}, {y})")

# Create a listener for keyboard events
def on_press(key):
    if key == keyboard.Key.esc:
        # Stop the listener by returning False
        return False

# Start the listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Loop until 'esc' key is pressed
while listener.is_alive():
    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Iterate over each pixel on the screen
    for x in range(screen_width):
        for y in range(screen_height):
            # Check if the pixel is white
            if is_pixel_white(x, y):
                # Click the pixel if it's white
                human_like_click(x, y)

    # Add a small delay between iterations
    pyautogui.sleep(0.1)

# Stop the listener
listener.stop()
