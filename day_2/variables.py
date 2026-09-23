#Day 2 : 30 Days Of Python Programming
firstname = "Ayşenur"
lastname = "ÖZ"
fullname = firstname +" " + lastname
country = "Türkiye"
city = "Sakarya"
age = 22
year = 2026
is_married = False
is_true = True
is_light_on = True
x = y = z = 50

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(len(firstname))

print(firstname == lastname)

num1 = 5
num2 = 4

total = num1 + num2
diff = num1 - num2
product = num1 * num2
division = num1 / num2
remainder = num1 % num2
floor_division = num1 // num2

PI = 3.14
radius = 30 

area_of_circle = PI * radius * radius
circum_of_circle = 2 * PI * radius 

radius = float(input("enter a radius value: "))
print("Area of circle: ", PI * radius * radius)

firstname = str(input("enter your firstname: "))
lastname = str(input("enter your lastname:"))
country = str(input("enter your country:"))
age = int(input("enter your age:"))

print("your name is", firstname, lastname)
print("you are", age, "years old")
print("you are from", country)