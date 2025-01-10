import pyautogui
import time


message = "skill issue"


repeat = 500


print("You have 5 seconds to focus on WhatsApp Desktop app")
time.sleep(5)


for _ in range(repeat):
    pyautogui.typewrite(message)
    pyautogui.press("enter")

print("Messages sent!")
