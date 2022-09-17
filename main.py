import time
from utils import getAveragePricesForItemName

start = time.time()

items = [
    'Pyerite',
    'Zydrine',
    'Mexallon',
    'Tritanium',
    'Opulent Compound',
    'Heavy Metals',
    'Heavy Water',
    'Plasmoids'
]

for item in items:
    average = getAveragePricesForItemName(item)
    print('\nThe average price of {name} is {price} ISK.\n'.format(name=item, price=average))

end = time.time()
print('Finished in {}'.format(end-start))
    
