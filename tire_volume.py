"""
Formula
v = 3.14 * w**2 * a * (w * a + 2540 * d)/10000000000
"""
# import libraries
from datetime import datetime
import math

# price variable to store price of tire
price = 0.00
print()

# Gathering tire information from user
w = int(input("Enter the width of the tire in mm: "))
a = int(input("Enter the aspect ratio of the tire: "))
d = int(input("Enter the diameter of the wheel in inches: "))

# determine price of tire
# The prices here are merely median prices for these size ranges
# Not actual prices 
if d <= 15:
    price = 115.00
elif d > 15 or d == 20:
    price = 250.00
elif d > 20 or d == 26:
    price = 320.00

# apply the formula for volume
part_1 = math.pi * w**2 * a * (w * a + 2540 * d)
v = part_1 / 10000000000
print()

# print result and price
print(f"The approximate volume is {v:.2f} liters.")
print(f"Price of Tire: ${price:.2f}")
print()

# Ask for purchase or no purchase
buy = input("Would you like to buy this tire? (yes/no): ")

# using .now and .strftime(with arguments) to clean up datetime 
# so it would only display the date and not the time
dateTime = datetime.now()
dateOnly = dateTime.strftime("%Y-%m-%d")

# If the user decides to buy the tire, it should print to the txt file
# If user decides not to buy, it will not print to txt file
if buy == "yes":
    
    phone = input("Please enter your phone number: ")
    print()
    print("Thank you for your purchase! Your receipt is being printed.")
    
    with open("volumes.txt", "at") as volumes_file:
        print(f"{dateOnly}, {w}, {a}, {d}, {v:.2f}, {phone}",file=volumes_file)
        
else: # User input "no" will not print to txt file!
    print("Thank you! Come again!")
