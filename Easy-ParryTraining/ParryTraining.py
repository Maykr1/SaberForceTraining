import pyautogui
import keyboard
import random
import time

min_interval = 1 #seconds
max_interval = 2 #seconds

print("Parry-Training Script started. Press '5' to stop.") #Cannot be in IDE, textbox, chatbox, or anything when pressing 5

try:
    while True:
        if keyboard.is_pressed('5'):
            print("Exiting Parry-Training Script")
            break

        pyautogui.click()

        #Generates a floating point number between min_interval and max_interval
        interval = random.uniform(min_interval, max_interval)
        time.sleep(interval)

except KeyboardInterrupt: #If user pressed Ctrl + C (Cmd + C on Max) in terminal, script stops
    print("Parry-Training Script stopped by user.")