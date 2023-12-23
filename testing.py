# Import the libraries
import pyautogui
import time
import pytesseract
from PIL import ImageGrab
from PIL import Image
import random
import pyscreeze
import PIL

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

sw, sh = pyautogui.size()

middleOfSCreen= (sw/2, sh/2)

time.sleep(1)
if(pyautogui.locateCenterOnScreen("3manaLeft.png",  confidence=0.5)!=None):
    threeMana=pyautogui.locateCenterOnScreen("3manaLeft.png",  confidence=0.5)
    tm1=(threeMana.x/2, threeMana.y/2)
    pyautogui.moveTo(tm1,None,1)
    pyautogui.dragTo(middleOfSCreen, button='left', duration=1)


