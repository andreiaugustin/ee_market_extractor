from time import sleep
import pyautogui
from PIL import ImageGrab
from AppKit import NSWorkspace
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID
)

default_wait_time = .7

def findWindowByOwner(pOwnerName):
    windowList = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
    for window in windowList:
        if window['kCGWindowOwnerName'] == pOwnerName:
            return window['kCGWindowBounds']
    return {}

def capture(pRect):
    capture = ImageGrab.grab()
    return capture.crop(pRect)

def click(pCoords, pWait=default_wait_time):
    pyautogui.click(pCoords)
    sleep(pWait)
    
def write(pText, pWait=default_wait_time):
    pyautogui.typewrite(pText)
    sleep(pWait)
    
def hotkey(pKey, pWait=default_wait_time):
    pyautogui.hotkey(pKey)
