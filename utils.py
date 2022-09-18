
import numpy as np
from ee import getWindowName, setupCoordinates
from ocr import getTextFromImage
from window import (
    findWindowByOwner, 
    capture, 
    click, 
    write,
    hotkey
)

def getAveragePriceFromText(pText):
    numbers = []
    text = pText.split('\n\n')
    for price in text:
        if len(price):
            numbers.append(
                int(
                    str(price[:-2])
                    .replace(".","")
                    .replace(",","")
                    .replace("/","")
                    )
                )
    if len(numbers):
        return round(sum(numbers) / len(numbers))
    return 0

def getAveragePricesForItemName(pName):
    rect = findWindowByOwner(getWindowName())
    if not len(rect):
        print('\nWindow {} was not found.\n'.format(getWindowName()))
        exit(1)
    coordinates = setupCoordinates(rect)
    
    click(coordinates['bring_to_front'])
    click(coordinates['open_menu'])
    click(coordinates['menu_market'], 2)
    click(coordinates['market_open_search'], 2)
    write(pName)
    hotkey('esc', 2)
    click(coordinates['market_search_btn'], 5)
    click(coordinates['market_first_result'], 4)
    pic = capture(( # first three prices coordinates
        (rect['X']+800)*2,
        (rect['Y']+370)*2,
        (rect['X']+1025)*2,
        (rect['Y']+680)*2
    )) # times two everything as we're using retina displays
    click(coordinates['market_book_exit'])
    click(coordinates['market_exit'])
    return getAveragePriceFromText(getTextFromImage(np.array(pic)))