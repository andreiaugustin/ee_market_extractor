from utils import getAveragePricesForItemName
import json

items = [
    'Nocxium',
    'Pyerite',
    'Zydrine',
    'Mexallon',
    'Tritanium',
    'Megacyte',
    'Isogen'
]

average_prices = []

for item in items:
    average = getAveragePricesForItemName(item)
    average_prices.append({item:average})
    
with open('./data/minerals_prices.json', 'w+') as f:
    f.write(json.dumps(average_prices))
