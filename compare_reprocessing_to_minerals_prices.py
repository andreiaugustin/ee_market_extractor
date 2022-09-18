import json

minerals_prices = []
modules_prices = []

isogen = []
megacyte = []
mexallon = []
nocxium = []
pyerite = []
tritanium = []
zydrine = []

with open('./data/minerals_prices.json') as f:
    minerals_prices = json.load(f)
    
with open('./data/modules_prices.json') as f:
    modules_prices = json.load(f)

with open('./data/static/reprocessing/isogen.json') as f:
    isogen = json.load(f)
    if not len(isogen):
        print('No data for Isogen was found.')
        exit(1)

with open('./data/static/reprocessing/megacyte.json') as f:
    megacyte = json.load(f)
    if not len(megacyte):
        print('No data for Megacyte was found.')
        exit(1)

with open('./data/static/reprocessing/mexallon.json') as f:
    mexallon = json.load(f)
    if not len(mexallon):
        print('No data for Mexallon was found.')
        exit(1)

with open('./data/static/reprocessing/nocxium.json') as f:
    nocxium = json.load(f)
    if not len(nocxium):
        print('No data for Nocxium was found.')
        exit(1)

with open('./data/static/reprocessing/pyerite.json') as f:
    pyerite = json.load(f)
    if not len(pyerite):
        print('No data for Pyerite was found.')
        exit(1)

with open('./data/static/reprocessing/tritanium.json') as f:
    tritanium = json.load(f)
    if not len(tritanium):
        print('No data for Tritanium was found.')
        exit(1)

with open('./data/static/reprocessing/zydrine.json') as f:
    zydrine = json.load(f)
    if not len(zydrine):
        print('No data for Zydrine was found.')
        exit(1)
        
def getValueFromListDict(pList, pName):
    return next((item for item in pList if list(item.keys())[0] == pName), 0)

def getValueFromListDictDict(pList, pName):
    val = getValueFromListDict(pList, pName)
    if val != 0:
        return val[pName]
    return 0
        
for module in modules_prices:
    name = list(module.keys())[0]
    price = module[name]
    
    # get all yield prices
    isogen_yield_price = (getValueFromListDictDict(isogen, name) *
                    getValueFromListDictDict(minerals_prices, 'Isogen'))
    
    megacyte_yield_price = (getValueFromListDictDict(megacyte, name) *
                    getValueFromListDictDict(minerals_prices, 'Megacyte'))
    
    mexallon_yield_price = (getValueFromListDictDict(mexallon, name) *
                    getValueFromListDictDict(minerals_prices, 'Mexallon'))
    
    nocxium_yield_price = (getValueFromListDictDict(nocxium, name) *
                    getValueFromListDictDict(minerals_prices, 'Nocxium'))
    
    pyerite_yield_price = (getValueFromListDictDict(pyerite, name) *
                    getValueFromListDictDict(minerals_prices, 'Pyerite'))
    
    tritanium_yield_price = (getValueFromListDictDict(tritanium, name) *
                    getValueFromListDictDict(minerals_prices, 'Tritanium'))
    
    zydrine_yield_price = (getValueFromListDictDict(zydrine, name) *
                    getValueFromListDictDict(minerals_prices, 'Zydrine'))
    
    # add them together
    yield_price = (isogen_yield_price+
                   megacyte_yield_price+
                   mexallon_yield_price+
                   nocxium_yield_price+
                   pyerite_yield_price+
                   tritanium_yield_price+
                   zydrine_yield_price
                   )
    
    # if the yield price of minerals is less than the price of the module, better off buying the module! 
    if price and (price<yield_price):
        print('\nBuying {module} for {module_price} and reprocessing with 5/5/5 would save {difference} ISK.\n'.format(module=name,module_price=price,difference=yield_price-price))