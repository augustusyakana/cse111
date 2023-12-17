# import library
from datetime import datetime

# datetime variables
dateTimeNow = datetime.now(tz=None)
day = dateTimeNow.weekday()

# declared variables
subtotal = float(input("Enter subtotal: "))
tenPercent = subtotal * (10 / 100)
tax = subtotal * (6 / 100)
difference = 50 - subtotal

if subtotal >= 50:
    if day == 1 or day == 2:
        total = (subtotal + tax) - tenPercent
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${tax:.2f}")
        print(f"Discount: ${tenPercent:.2f}")
        print(f"Total: ${total:.2f}")
    
    else:
        total = subtotal + tax
        print(f"Discount not applicable today.")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")
    print()

# amount not equal to $50 or more
else:
    print("In order to receive the discount, your subtotal should amount to $50 or more.")
    print(f"You need ${difference:.2f} more to be qualified for said discount.")