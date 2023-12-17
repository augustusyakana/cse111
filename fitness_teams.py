# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender (m/f): ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    height = float(input("Enter your height in US inches: "))
    weight = float(input("Enter your weight in US pounds: "))

    # Call the compute_age, kg_from_lb, cm_from_in,
    age = compute_age(birth_str=dob)
    kg = kg_from_lb(pounds=weight)
    cm = cm_from_in(inches=height)
    
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    bmi = body_mass_index(weight=kg, height=cm)
    bmr = basal_metabolic_rate(gender=gender, weight=kg, height=cm, age=age)
    
    # Print the results for the user to see.
    print(f"Age: {age}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body Mass Index: {bmi:.1f}")   
    print(f"Basal Metabolic Rate (kcal/day): {bmr:.0f}")
    
def compute_age(birth_str):
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    return kg

def cm_from_in(inches):
    cm = inches * 2.54
    return cm

def body_mass_index(weight, height):
    bmi = 10000 * weight / height**2
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    if gender.lower() == "f":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age 
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr

main()
# Call the main function so that
# this program will start executing.
