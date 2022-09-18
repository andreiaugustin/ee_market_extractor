import time
from utils import getAveragePricesForItemName

items = [
    # # ,'MK9 Large Shield Field Module'
    # # ,'MK9 Large Armor Link Module'
    # # ,'MK9 Large Group Shield Booster'
    # # ,'MK9 Large Group Armor Repairer'
    # # ,'MK9 Large Group Capacitor Transmitter'
    # # ,'MK7 Large Shield Field Module'
    # 'MK7 Large Armor Link Module'
    # ,'MK9 Large Energy Nosferatu'
    # ,'MK9 Large Energy Neutralizer'
    # ,'MK9 Covert Ops Cloaking Device'
    # ,'MK9 Large Shield Extender'
    # ,'MK9 1600mm Reinforced Steel Plate'
]

average_prices = []

for item in items:
    average = getAveragePricesForItemName(item)
    average_prices.append({item:average})

print(average_prices)