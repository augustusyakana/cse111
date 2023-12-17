import random

def main():
    numbers = [16.2, 75.1, 52.3]

    print(f"Numbers: {numbers}")
    
    append_random_numbers(numbers)
    print(f"Numbers: {numbers}")
    
    append_random_numbers(numbers, 3)
    print(f"Numbers: {numbers}")
    

def append_random_numbers(numbers_list, quantity):
    
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded_number = round(random_number, 1)
        numbers_list.append(rounded_number)
        
if __name__ == "__main__":
    main()