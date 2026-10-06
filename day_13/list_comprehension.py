numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in numbers if i < 0]
print("Negative numbers:", negative_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [num for lst in list_of_lists for num in lst]
print("Flatten numbers =",flatten_list)

list_of_tuples = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4 , i ** 5) for i in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_countries = [[coun_tuple[0].upper(),coun_tuple[0][0:3].upper(),coun_tuple[1].upper()] for country in countries for coun_tuple in country ]
print(list_of_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_of_countries = [{"country": coun_tuple[0], "city": coun_tuple[1]} for country in countries for coun_tuple in country]
print(dict_of_countries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name_list = [' '.join(name) for fullname in names for name in fullname]
print(name_list)