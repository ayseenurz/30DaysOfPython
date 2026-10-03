from countries_data import countries_data

def add_two_numbers(num1,num2):
    return print(num1,"+",num2,"=",num1+num2)
add_two_numbers(3,4)

def area_of_circle(r):
    pi = 3.14
    return pi * r * r
print("The area of the circle:",area_of_circle(5))

def add_all_numbers(*args):
    total = 0
    for num in args:
        if type(num) != int and type(num) != float:
            print(num,"is not a number, the process wont be continued.")
            return None
        total += num
    return total
print("The sum of all numbers:",add_all_numbers(1,2,3,4,"a",6,7,8,9,10))

def convert_celsius_to_fahrenheit(cel):
    return (cel * 9/5) + 32
print("The temperature in Fahrenheit:",convert_celsius_to_fahrenheit(37))

def check_season(month):
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    elif month in ["September", "October", "November"]:
        return "Autumn"
    else:
        return "Invalid month"
print("The season is:",check_season("March"))

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)
print("The slope of the line is:",calculate_slope(1, 2, 3, 4))

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)
print("The roots of the quadratic equation are:",solve_quadratic_eqn(1, -3, 2))

list = [1, 2, 3, 4, 5]
def print_list_elements(lst):
    for element in lst:
        print(element)
print("The elements of the list are:")
print_list_elements(list)

def reverse_list(lst):
    return lst[::-1]
print("The reversed list is:",reverse_list(["A", "B", "C"]))

list2 = ["python", "numpy", "Pandas", "Django", "Flask"]

def capitalize_list_elements(lst):
    return [element.capitalize() for element in lst]
print("The capitalized list elements are:",capitalize_list_elements(list2))

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
def add_item(lst, *items):
    for item in items:
        lst.append(item)
    return lst
print("The updated list after adding an item is:",add_item(food_stuff, "Meat", "Eggs"))

def remove_item(lst, *items):
    for item in items:
        if item in lst:
            lst.remove(item)
    return lst
print("The updated list after removing an item is:",remove_item(food_stuff, "Mango", "Milk"))

def sum_of_numbers(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total
print("The sum of numbers from 0 to 100 is:",sum_of_numbers(100))

def sum_of_odds(num):
    total = 0
    for i in range(num + 1):
        if i % 2 != 0:
            total += i
    return total
print("The sum of odd numbers from 0 to 100 is:",sum_of_odds(100))

def sum_of_evens(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            total += i
    return total
print("The sum of even numbers from 0 to 100 is:",sum_of_evens(100))

def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for i in range(num + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
even_count, odd_count = evens_and_odds(100)
print("The number of even numbers from 0 to 100 is:",even_count)
print("The number of odd numbers from 0 to 100 is:",odd_count)

def factorial(num):
    res = num
    if num < 0 :
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return print("The factorial of", num, "is:", 1)
    else:
        for i in range(num - 1, 0, -1):
            res *= i
    return print("The factorial of", num, "is:", res)
factorial(0)

def is_empty(arg):
    if arg == [] or arg == "" or arg == {} or arg == () or arg is None:
        return True
    else:
        return False
print("Is the list empty?",is_empty([]))

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        median = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        median = sorted_lst[n // 2]
    return median
print("The median of the list is:",calculate_median([1, 3, 3, 6, 7, 8, 9]))

def calculate_mean(lst):
    return sum(lst) / len(lst)
print("The mean of the list is:",calculate_mean([1, 2, 3, 4, 5]))

def calculate_range(lst):
    return max(lst) - min(lst)
print("The range of the list is:",calculate_range([1, 2, 3, 4, 5]))

def calculate_mode(lst):
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    mode = [key for key, value in frequency.items() if value == max_freq]
    return mode
print("The mode of the list is:",calculate_mode([1, 2, 2, 3, 3, 3, 4, 5]))

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)
print("The variance of the list is:",calculate_variance([1, 2, 3, 4, 5]))

def calculate_std(lst):
    variance = calculate_variance(lst)
    return variance ** 0.5
print("The standard deviation of the list is:",calculate_std([1, 2, 3, 4, 5]))

def greeting(name = "Guest"):
    return "Hello, " + name + "!"
print(greeting("Ayşenur"))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Is 7 a prime number?",is_prime(7))

def is_all_unique(lst):
    return len(lst) == len(set(lst))
print("Are all elements in the list unique?",is_all_unique([1, 2, 3, 4, 5]))

def is_all_same(lst):
    return all(x == lst[0] for x in lst)
print("Are all elements in the list the same?",is_all_same(["a", "a", "A", "a", "a"]))

def is_valid_variable(var):
    import keyword
    if not var.isidentifier() or keyword.iskeyword(var):
        return False
    return True
print("Is '3my_var' a valid variable name?",is_valid_variable("3my_var"))

def most_spoken_languages(countries_data, n):
    language_count = {}
    for country in countries_data:
        for language in country["languages"]:
            if language not in language_count:
                language_count[language] = 0
            language_count[language] += 1
    most_spoken_languages = sorted(
        language_count.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return most_spoken_languages[:n]

print("The most spoken languages are:", most_spoken_languages(countries_data, 10))

def most_populated_countries(countries_data, n):
    most_populated = sorted(
        countries_data,
        key=lambda country: country["population"],
        reverse=True
    )
    return [(country["name"], country["population"]) for country in most_populated[:n]]
print("The most populated countries are:", most_populated_countries(countries_data, 10))