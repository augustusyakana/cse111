# import math module

import math

numItems = int(input("Enter the number of items: "))
perBox = int(input("Enter the number of items per box: "))

numBox = math.ceil(numItems / perBox)

print(f"For {numItems} items, packing {perBox} items in each box, you will need {numBox} boxes.")