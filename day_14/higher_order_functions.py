import functools
from countries_data import countries_data
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst) 
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

# DECORATOR
# Normal function
'''
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

This decorator function is a higher order function
that takes a function as a parameter

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
'''
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#the difference between map, filter and reduce is the reduce function takes two parameters, 
# the first parameter is a function and the second parameter is a list. 
# The reduce function applies the function to the first two elements of the list and then applies the function to the result 
# and the next element of the list and so on until all elements are processed. The final result is a single value.

# the difference between higher order fuctions, decorators and closures is that higher order functions take a function as a parameter and return a function,
# decorators are a special type of higher order function that take a function as a parameter and return a function that adds some functionality to the original function, and closures are functions that are defined inside another

def add_two_numbers(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

lst = [1, 2, 3, 4, 5]


ad_numbers = list(map(add_two_numbers, numbers, numbers))
print("Add two numbers:", ad_numbers)

even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

total = functools.reduce(add_two_numbers, numbers)
print("Total:", total)

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

uppercase_countries = list(map(lambda x: x.upper(), countries))
print("uppercase_countries:",uppercase_countries)

squared_numbers = list(map(lambda x : x ** 2 , numbers))
print("squared_numbers:",squared_numbers)

with_land = list(filter(lambda x : 'land' in x, countries))
print("land countries:",with_land)

six_chars_countries = list(filter(lambda x: len(x) == 6, countries))
print("six charachter countries:", six_chars_countries)

six_and_more_letter_countries = list(filter(lambda x: len(x) >= 6, countries))
print("6 and more letter countries:", six_and_more_letter_countries)

starting_with_E = list(filter(lambda x : x.startswith('E'),countries))
print("Countries starting with E:",starting_with_E)

lst = [1, 3, 4, 5, 7, 8]
result = functools.reduce(lambda x, y: x + y, map( lambda x: x ** 2, filter(lambda x: x % 2 == 0, lst)))
print(result)

liste = [1, 3, 5,"Ahmet", 6,"Ayşenur"]
def get_string_lists(lst):
    return filter(lambda x : type(x) is str, lst)
string_list = get_string_lists(liste)
print(list(string_list))

def add_all_numbers(lst):
    return functools.reduce(lambda x, y: x + y, lst)

sum = add_all_numbers(numbers)
print(sum)

def make_sentence(lst):
    return functools.reduce(lambda x, y: f"{x}, {y}", lst) + " are north european countries"
sent = make_sentence(countries)
print(sent)

def categorize_countries(lst, pattern):
    return list(filter(lambda x: pattern in x,lst))
filtered_countries = categorize_countries(countries,"land")
print(filtered_countries)

def count_countries(lst):
    result = {}

    for country in lst:
        first_letter = country[0]

        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1

    return result


countries_count = count_countries(countries)
print(countries_count)

def get_first_ten_countries(lst):
    return lst[:10]

print(get_first_ten_countries(countries))

def get_last_ten_countries(lst):
    return lst[-10:]

print(get_last_ten_countries(countries))


# Ülkeleri isme göre sırala
sorted_by_name = sorted(
    countries_data,
    key=lambda country: country["name"]
)

print("Countries by name:")
for country in sorted_by_name:
    print(country["name"])


# Ülkeleri başkente göre sırala
sorted_by_capital = sorted(
    countries_data,
    key=lambda country: country["capital"]
)

print("\nCountries by capital:")
for country in sorted_by_capital:
    print(country["name"], "-", country["capital"])


# Ülkeleri nüfusa göre sırala
sorted_by_population = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True
)

print("\nCountries by population:")
for country in sorted_by_population:
    print(country["name"], "-", country["population"])


# En kalabalık 10 ülke
top_10_populated = sorted_by_population[:10]

print("\nTop 10 most populated countries:")
for country in top_10_populated:
    print(country["name"], "-", country["population"])


# Dilleri say
language_count = {}

for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1


# Dilleri konuşulma sayısına göre sırala
sorted_languages = sorted(
    language_count.items(),
    key=lambda x: x[1],
    reverse=True
)


# En çok konuşulan 10 dil
top_10_languages = sorted_languages[:10]

print("\nTop 10 most spoken languages:")
for language, count in top_10_languages:
    print(language, "-", count)