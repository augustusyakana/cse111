# Import datetime module from datetime library
from datetime import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("What is your gender? (M or F): ")
    dob = input("What is your date of birth? (YYYY-MM-DD): ")
    height = float(input("Enter your height in U.S. inches: "))
    weight = float(input("Enter your weight in U.S. pounds: "))

    # call the functions to be used: 
    age = int(compute_age(birth_str=dob))
    kilo = kg_from_lb(pounds=weight)
    centi = cm_from_in(inches=height)
    bmi = body_mass_index(weight=kilo, height=centi)
    bmr = basal_metabolic_rate(gender=gender, weight=kilo, height=centi, age=age)
    
    # Print the results for the user to see.
    print(f"Age: {age}")
    print(f"Weight (kg): {kilo:.2f}km")
    print(f"Height (cm): {centi:.1f}cm")
    print(f"Body Mass Index: {bmi:.1f}")
    print(f"Basal Metabolic Rate (kcal/day): {bmr:.0f}")
    

    # get the user's age using the data entered
def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    return years

    # convert pounds to kilograms
def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    return kg

    # convert inches to centimeters
def cm_from_in(inches):
    cm = inches * 2.54
    return cm

    # calculate the bmi using the weight and height provided 
def body_mass_index(weight, height):
    bMi = 10000 * weight / height**2
    return bMi

    # calculate bmr using gender, weight, height and age provided
def basal_metabolic_rate(gender, weight, height, age):
    if gender.lower() == "m":
        bMr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age 
    elif gender.lower() == "f":
        bMr = 447.593 + 9.247 * weight + 3.098 * height - 5.677 * age      
    return bMr

# call the main function so program can execute
main()