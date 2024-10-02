import pyautogui
import time

# 1. Moving the Mouse
def move_mouse():
    pyautogui.moveTo(100, 200, duration=1)
    pyautogui.move(50, 50, duration=0.5)

# 2. Getting the Mouse Position
def get_mouse_position():
    position = pyautogui.position()
    print(f"Current mouse position: {position}")
    return position

# 3. Clicking the Mouse
def click_mouse():
    pyautogui.click(150, 150)
    pyautogui.rightClick()
    pyautogui.doubleClick()

# 4. Dragging the Mouse
def drag_mouse():
    pyautogui.moveTo(100, 100)
    pyautogui.dragTo(200, 200, duration=1)
    pyautogui.drag(50, 50, duration=0.5)

# 5. Scrolling the Mouse
def scroll_mouse():
    pyautogui.scroll(500)
    pyautogui.scroll(-500)

# 6. Typing with the Keyboard
def type_text():
    pyautogui.click(300, 300)  # Ensure this clicks on a text field before running
    pyautogui.typewrite('Hello, World!', interval=0.1)

# 7. Pressing Keyboard Keys
def press_keys():
    pyautogui.press('enter')
    pyautogui.keyDown('shift')
    pyautogui.press('a')
    pyautogui.keyUp('shift')
    pyautogui.hotkey('ctrl', 'c')

# 8. Screenshot and Image Recognition
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    print("Screenshot saved as 'screenshot.png'")

def locate_image(image_path):
    location = pyautogui.locateOnScreen(image_path)
    if location:
        print(f"Image found at: {location}")
    else:
        print(f"Image '{image_path}' not found on screen.")
    return location

# 9. Getting Screen Size
def get_screen_size():
    screen_width, screen_height = pyautogui.size()
    print(f"Screen size: {screen_width}x{screen_height}")
    return screen_width, screen_height

# 10. Getting Center of Screen
def get_center_of_screen():
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    print(f"Center of the screen: ({center_x}, {center_y})")
    return center_x, center_y

# 11. Custom Alerts
def show_alert():
    pyautogui.alert('This is an alert message!')

def show_confirm():
    response = pyautogui.confirm('Do you want to proceed?')
    print(f"User response: {response}")
    return response

def show_prompt():
    user_input = pyautogui.prompt('Please enter your name:')
    print(f"User input: {user_input}")
    return user_input

# 12. Failsafe and Pauses
def demo_with_pause():
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5  # Adds a 0.5-second pause between PyAutoGUI calls
    pyautogui.moveTo(200, 200)
    pyautogui.click()

# 13. Mouse Position Relative to the Window
def get_mouse_relative():
    position = pyautogui.position()
    screen_width, screen_height = pyautogui.size()
    relative_x = position[0] / screen_width
    relative_y = position[1] / screen_height
    print(f"Mouse relative position: ({relative_x:.2f}, {relative_y:.2f})")
    return relative_x, relative_y
