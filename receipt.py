import csv
from datetime import datetime

def main():
    print(f"Inkom Emporium")
    print()
    try:
        # read_dictionary indexes
        KEY_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2
        
        # request indexes
        PRODUCT_NUMBER_INDEX = 0
        QUANTITY_INDEX = 1
        
        current_date_and_time = datetime.now()
        day = current_date_and_time.weekday()
        
        product_dict = read_dictionary(filename="products.csv", key_column_index=KEY_INDEX)
        
        request_list = []
        with open ("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            num_items = 0
            subtotal = 0.00
            print("Requested Items:")
            for row_list in reader:
                product_number = row_list[PRODUCT_NUMBER_INDEX]
                quantity = int(row_list[QUANTITY_INDEX])
                request_list.append(row_list)  
                
                product = product_dict[product_number]       
                name = product[NAME_INDEX]
                price = float(product[PRICE_INDEX])
                
                num_items += quantity             
                print(f"{name}: {quantity}x @ ${price}")
                
                subtotal += (price * quantity)
                discount = subtotal * (10 / 100)   
                sales_tax = subtotal * (6 / 100) 
                
            if day < 1 or day > 2:
                total = subtotal + sales_tax
                print()
                print(f"Number of Items: {num_items}")
                print(f"Subtotal: ${subtotal:.2f}")
                print(f"Sales Tax: ${sales_tax:.2f}")
                print(f"Total: ${total:.2f}")
                print()
            else:
                total = (subtotal + sales_tax) - discount
                print()
                print(f"Number of Items: {num_items}")
                print(f"Subtotal: ${subtotal:.2f}")
                print(f"Sales Tax: ${sales_tax:.2f}")
                print(f"Discount: ${discount:.2f}")
                print(f"Total: ${total:.2f}")
                print()
                
            print(f"Thank You for shopping at Inkom Emprium")
            print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
                
            
        
    except KeyError as key_err:
        print()
        print(f"Error: Unknown product in the request.csv file" 
                f"'{key_err}'")
        
    except FileNotFoundError as no_file_err:
        print(f"Error: Missing file")
        print(f"{no_file_err}")

def read_dictionary(filename, key_column_index):

        
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open (filename, 'rt') as product_dict:
        reader = csv.reader(product_dict)
        next(reader)
        
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary
        
if __name__ == "__main__":
    main()