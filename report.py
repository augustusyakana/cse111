

numOfProjects = int(input("How many cars you will service today? "))

print()
print(f'Today you are servicing {numOfProjects} cars!')

jayNum = int(input("Hi Jay, how many cars did you service today? "))

percentage = jayNum / numOfProjects * 100
print()
print(f'Jay, you completed {percentage:.0f}% of projects today!')