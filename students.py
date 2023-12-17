import csv


def main():
    
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    dictionary = read_dictionary(filename="students.csv", key_column_index=I_NUMBER_INDEX)
  
    i_number = input("Enter Student I-Number:")
    
    i_number = i_number.replace("-", "")
    
    if not i_number.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(i_number) < 9:
            print("Invalid I-Number: too few digits")
        elif len(i_number) > 9:
            print("Invalid I-Number: too many digits")
        else:
            if i_number not in dictionary:
                print("No such student")
            else:
                value = dictionary[i_number]
                name = value[NAME_INDEX]
                print(name)
    


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
    with open (filename, "rt") as students_file:
        reader = csv.reader(students_file)
        next(reader)
        
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

        return dictionary

if __name__ == "__main__":
    main()