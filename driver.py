import random
import pyautogui
import time

# get the width and height of the screen
width, height = pyautogui.size()

#time array
timeIntervals = [60, 120, 180, 240, 300]

while(True):
	randX = random.randint(0, width)
	randY = random.randint(0, height)
	print(randX, randY)

	waitTime = random.randint(0, len(timeIntervals))

	pyautogui.moveTo(randX, randY, 1)
	time.sleep(timeIntervals[waitTime])













