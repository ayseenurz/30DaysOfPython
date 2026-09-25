word1 = "Thirty"
word2 = "Days"
word3 = "Of"
word4 = "Python"
blank = " "
full_sentence = word1 + blank + word2 + blank + word3 + blank + word4
word5 = "Coding"
word6 = "For"
word7 = "All"
full_sentence2 = word5 + blank + word6 + blank + word7
print(full_sentence)
print(full_sentence2)

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower()) 
print(company.capitalize())
print(company.title())
print(company.swapcase())  
print(company[7:])
print(company.index("Coding"))
print(company.rindex("Coding"))
print(company.find("Coding"))
print(company.rfind("Coding"))
print(company.replace("Coding", "Python"))

sentence = "Python for Everyone"
print(sentence.replace("Everyone", "All"))
print(company.split(" "))

some_brands = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(some_brands.split(","))

print(company[0])
print(company[-1])
print(company[10])

acronym1 = company[0] + company[7] + company[11]
print(acronym1)

acronym2 = sentence[0] + sentence[7] + sentence[11] 
print(acronym2)

print(company.index("C"))
print(sentence.index("f"))
print(company.rfind("i"))

new_sentence = 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.index("because"))
print(new_sentence.rindex("because"))
print(new_sentence[31:54])
print(new_sentence.find("because"))

sub_String = "Coding"
sub_string2 = "coding"
print(company.startswith(sub_String))
print(company.endswith(sub_string2))

print('   Coding For All      ' .strip())

print("thirt_days_of_python".isidentifier())
print("30DaysOfPython".isidentifier())

libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libs))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

num_1 = 8
num_2 = 6
print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
print("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
print("{} * {} = {}".format(num_1, num_2, num_1 * num_2))
print("{} / {} = {:.2f}".format(num_1, num_2, num_1 / num_2))
print("{} % {} = {}".format(num_1, num_2, num_1 % num_2))
print("{} // {} = {}".format(num_1, num_2, num_1 // num_2))
print("{} ** {} = {}".format(num_1, num_2, num_1 ** num_2))