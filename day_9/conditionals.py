your_age = int(input("Enter your age: "))
if your_age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - your_age
    print(f"You need to wait {years_left} more years to drive.")

my_age = 22
if my_age > your_age:
    print(f"I am {my_age - your_age} years older than you.")
elif my_age < your_age:
    print(f"You are {your_age - my_age} years older than me.")
else:
    print("We are the same age.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is less than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")


your_grade = int(input("Enter your grade (0-100): "))

if your_grade >= 90:
    print("Your grade is A.")
elif your_grade >= 80:
    print("Your grade is B.")
elif your_grade >= 70:
    print("Your grade is C.")
elif your_grade >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")       

curr_month = str(input("Enter the current month: ")).lower()
if curr_month in ["september", "october", "november"]:
    print("The season is Autumn.")
elif curr_month in ["december", "january", "february"]:
    print("The season is Winter.")
elif curr_month in ["march", "april", "may"]:
    print("The season is Spring.")
elif curr_month in ["june", "july", "august"]:
    print("The season is Summer.")

fruits = ["banana", "orange", "mango", "lemon"]
fruit_to_check = str(input("Enter a fruit to check: ")).lower()
if fruit_to_check in fruits:
    print(f"{fruit_to_check} is already in the list.")
else:
    fruits.append(fruit_to_check)
    print(f"{fruit_to_check} has been added to the list.")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print(f"Skills: {person['skills'][len(person['skills'])//2]}")  # Print the middle skill

if 'Python' in person['skills']:
    print("Python is present in the skills.")

if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print("She is a front-end developer.")
elif 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print("She is a back-end developer.")
elif 'React' in person['skills'] and 'Node' in person['skills']:
    print("She is a full-stack developer.")
else:
    print("Unknown title.")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")