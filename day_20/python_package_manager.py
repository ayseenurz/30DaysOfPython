from collections import Counter
import statistics
import requests
import re
from bs4 import BeautifulSoup

romeo_and_juliet = "https://www.gutenberg.org/files/1112/1112.txt"

response = requests.get(romeo_and_juliet)
text = response.text

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

word_counts = Counter(words)

print(word_counts.most_common(10))

cats_api = "https://api.thecatapi.com/v1/breeds"

response = requests.get(cats_api)
cats = response.json()

print(cats[0])


def range_midpoint(value):
    low, high = map(float, value.split(" - "))
    return (low + high) / 2

weights = [
    range_midpoint(cat["weight"]["metric"])
    for cat in cats
    if cat.get("weight", {}).get("metric")
    and " - " in cat["weight"]["metric"]
]

lifespans = [
    range_midpoint(cat["life_span"])
    for cat in cats
    if cat.get("life_span") and " - " in cat["life_span"]
]

for name, values in [
    ("Weight (kg)", weights),
    ("Lifespan (years)", lifespans)
]:
    print(name)
    print("Min:", min(values))
    print("Max:", max(values))
    print("Mean:", statistics.mean(values))
    print("Median:", statistics.median(values))
    print("Standard deviation:", statistics.stdev(values))


countries = Counter(
    cat["origin"]
    for cat in cats
    if cat.get("origin")
)

breeds_by_country = {}

for cat in cats:
    country = cat.get("origin")
    breed = cat.get("name")

    if country and breed:
        breeds_by_country.setdefault(country, []).append(breed)

print("Country frequency:")
print(countries.most_common())

print("\nBreeds by country:")
for country, breeds in breeds_by_country.items():
    print(country, ":", ", ".join(breeds))


url = "https://restcountries.com/v3.1/all?fields=name,area,languages,population"

response = requests.get(url)
countries = response.json()

largest_countries = sorted(
    [country for country in countries if country.get("area") is not None],
    key=lambda country: country["area"],
    reverse=True
)

for country in largest_countries[:10]:
    print(country["name"]["common"], country["area"])

all_languages = set()

for country in countries:
    all_languages.update(
        country.get("languages", {}).values()
    )

print("Total unique languages:", len(all_languages))


url = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)
print(soup.get_text(" ", strip=True)[:1000])