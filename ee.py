'''
Y coordinates have 25 removed due to macOS top-bar
'''
def setupCoordinates(pWindow):
    x = pWindow['X']
    y = pWindow['Y']
    return {
        'open_menu':(x+65, y+85), # Click on the top-left corner to open the menu
        'bring_to_front':(x+35, y+30), # Click under the yellow box of the window
        'menu_market':(x+480, y+275), # Click on the market option in the menu
        'market_open_search':(x+980, y+87), # Click on the market search option
        'market_search_btn':(x+1160, y+80), # Click on the market start searching button
        'market_search_clear_btn':(x+1120, y+80), # Click on the market search clear button (from results page)
        'market_book_exit':(x+1120, y+80), # Click outside the market book window to exit
        'market_first_result':(x+540, y+140), # Click on first result from market search
        'market_exit':(x+1300, y+85), # Click on X to exit market
        'close_keyboard':(x+505, y+785) # Click on close keyboard button
    }
    
def getWindowName():
    return 'BlueStacks'