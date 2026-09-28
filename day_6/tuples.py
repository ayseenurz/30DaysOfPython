mt_tuple = ()

sisters = ('beyza', 'zeynep', 'mamacita', 'miyav')
brothers = ('edi', 'büdü', 'ahmet')
siblings = sisters + brothers 
print(siblings)

print(len(siblings))

family_members = siblings + ('emine', 'sevgin')
print(family_members)

siblings = family_members[:7]
parents = family_members[7:]
print(siblings)
print(parents) 

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
animal_products = ('milk', 'meat', 'butter', 'yogurt')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_list = list(food_stuff_tp)
print(food_stuff_list)

first_part = food_stuff_list[0:3]
print(first_part)
last_part = food_stuff_list[-3:]
print(last_part)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)