def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    fruit_list.reverse()
    print(f"Reversed: {fruit_list}")
    
    fruit_list.append("orange")
    print(f"With Orange: {fruit_list}")
    
    i = fruit_list.index("apple")
    fruit_list.insert(i, "cherry")
    print(f"With cherry: {fruit_list}")
    
    fruit_list.remove("banana")
    print(f"Without banana: {fruit_list}")
    
    element = fruit_list.pop()
    print(f"Popped: {element}")
    print(f"after pop: {fruit_list}")
    
    fruit_list.sort()
    print(f"Sorted list: {fruit_list}")
    
    fruit_list.clear()
    print(f"Cleared: {fruit_list}")
    
if __name__ == "__main__":
    main()