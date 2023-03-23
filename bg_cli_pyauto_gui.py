
# https://www.geeksforgeeks.org/run-shell-command-from-gui-using-python/

# import required modules
import os
import pyautogui

# prompts message on screen and gets the command
# value in val variable
value = pyautogui.prompt("Enter Shell Command")

# executes the command and returns
# the output in stream variable
stream = os.popen(value)

# reads the output from stream variable
out = stream.read()
pyautogui.alert(out)
