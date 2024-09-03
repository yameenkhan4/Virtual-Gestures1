import pyautogui as p
from time import sleep
import pydirectinput as pd

for i in range(3):
    print(f"Strating in {i} seconds")
    sleep(1)

p.press('w')
pd.press('w')
sleep(3)

p.keyDown('w')
pd.keyDown('w')
sleep(3)
p.keyUp('w')
pd.keyUp('w')



