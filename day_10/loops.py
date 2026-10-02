from data.countries import countries
from data.countries_data import countries_data
'''count = 11
i = 0
for i in range(count):
    print(i)
    i += 1
i = 0
while i < 11:
    print(i)
    i += 1

revcount = 10

for revcount in range(i):
    i = i - 1
    print("i",i)


for i in range(8):
    print(i*"#")

print("\n")

for i in range(9):
        for j in range(9):
            if j == 8:
                print(j * "# ")

for i in range(11):
     for j in range(11):
          if i == j:
            print(i,"x",j,"=",(i*j))

list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in range(len(list)):
     print(list[i])
'''


for i in range(101):
    if i % 2 == 0:
        print(i)
for i in range(101):
    if i % 2 != 0:
        print(i)

toplam = 0
for i in range(101):
    toplam = toplam + i
print("0'dan 100'e kadar olan sayıların toplamı:",toplam)

even_sums = 0
odd_sums = 0 
for i in range(101):
    if i % 2 == 0 :
        even_sums = even_sums + i
    if i % 2 != 0 :
        odd_sums = odd_sums + i
print("The sum of the even numbers :",even_sums)
print("The sum of the odd numbers :",odd_sums)

for country in countries:
    if "land" in country:
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruits)):
    print(len(fruits)-i,". eleman:",fruits[len(fruits)-i-1])

languages = set()
for country in countries_data:
    country_languages = country["languages"]
    for language in country_languages:
        languages.add(language)
print("Toplam farklı dil sayısı:", len(languages))

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

print("\nEn çok konuşulan 10 dil:")

for language, count in most_spoken_languages[:10]:
    print(language, "->", count, "ülke")

most_populated_countries = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True
)

print("\nDünyanın en kalabalık 10 ülkesi:")

for country in most_populated_countries[:10]:

    print(country["name"], "->", country["population"])