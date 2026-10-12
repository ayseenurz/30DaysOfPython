import re
import json
from collections import Counter
from pathlib import Path
from data.stop_words import stop_words
import csv


def count_lines_and_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    words = text.split()

    return len(lines), len(words)

print(count_lines_and_words("data/obama_speech.txt"))
print(count_lines_and_words("data/michelle_obama_speech.txt"))
print(count_lines_and_words("data/donald_speech.txt"))
print(count_lines_and_words("data/melina_trump_speech.txt"))

def most_spoken_languages(filename, n):
    with open(filename, "r", encoding="utf-8") as file:
        countries = json.load(file)

    language_count = {}

    for country in countries:
        for language in country["languages"]:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    sorted_languages = sorted(
        language_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return [
        (count, language)
        for language, count in sorted_languages[:n]
    ]

print(most_spoken_languages("./data/countries_data.json", 10))
print(most_spoken_languages("./data/countries_data.json", 3))

def most_populated_countries(filename, n):
    with open(filename, "r", encoding="utf-8") as file:
        countries = json.load(file)

    sorted_countries = sorted(
        countries,
        key=lambda country: country["population"],
        reverse=True
    )

    return [
        {
            "country": country["name"],
            "population": country["population"]
        }
        for country in sorted_countries[:n]
    ]

print(most_populated_countries("./data/countries_data.json", 10))
print(most_populated_countries("./data/countries_data.json", 3))


def extract_emails(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    emails = re.findall(
        r'\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b',
        text
    )

    return emails

emails = extract_emails("./data/email_exchanges_big.txt")
print(emails)


def find_most_common_words(source, n):

    try:
        path = Path(source)
        if path.is_file():
            text = path.read_text(encoding="utf-8")
        else:
            text = source
    except (OSError, ValueError):
        text = source

    words = re.findall(r"\b\w+\b", text)

    word_counts = Counter(words)

    return word_counts.most_common(n)

print(find_most_common_words("./data/sample.txt", 10))
print(find_most_common_words("./data/sample.txt", 5))


def find_most_frequent_words(filename, n):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = re.findall(r"\b\w+\b", text.lower())
    word_counts = Counter(words)

    return word_counts.most_common(n)

print("Obama:")
print(find_most_frequent_words("data/obama_speech.txt", 10))

print("\nMichelle Obama:")
print(find_most_frequent_words("data/michelle_obama_speech.txt", 10))

print("\nDonald Trump:")
print(find_most_frequent_words("data/donald_speech.txt", 10))

print("\nMelania Trump:")
print(find_most_frequent_words("data/melina_trump_speech.txt", 10))


def read_text(source):
    """Dosya yolu verilirse dosyayı, değilse metni döndürür."""
    if isinstance(source, str):
        try:
            path = Path(source)
            if path.is_file():
                return path.read_text(encoding="utf-8")
        except (OSError, ValueError):
            pass

    return source


def clean_text(text):
    text = read_text(text)
    text = text.lower()
    words = re.findall(r"\b[a-z]+\b", text)
    return words


def remove_support_words(text):
    words = clean_text(text)
    stop_words_set = set(stop_words)

    return [
        word for word in words
        if word not in stop_words_set
    ]


def check_text_similarity(text1, text2):
    words1 = set(remove_support_words(text1))
    words2 = set(remove_support_words(text2))

    common_words = words1 & words2
    all_words = words1 | words2

    if not all_words:
        return 0.0, []

    similarity = len(common_words) / len(all_words) * 100

    return round(similarity, 2), sorted(common_words)

similarity, common_words = check_text_similarity(
    "data/michelle_obama_speech.txt",
    "data/melina_trump_speech.txt"
)

print("Similarity:", similarity, "%")
print("Common words:", common_words)


print(
    find_most_frequent_words(
        "data/romeo_and_juliet.txt",
        10
    )
)



with open("data/hacker_news.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader, None)  # Başlık satırını atla

    count = 0

    for row in reader:
        line = " ".join(row)

        if "python" in line.lower():
            count += 1

print("Python içeren satır sayısı:", count)

with open("data/hacker_news.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader, None)

    count = 0

    for row in reader:
        line = " ".join(row)

        if "javascript" in line.lower():
            count += 1

print("JavaScript içeren satır sayısı:", count)


with open("data/hacker_news.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader, None)

    count = 0

    for row in reader:
        line = " ".join(row).lower()

        if "java" in line and "javascript" not in line:
            count += 1

print("Java var, JavaScript yok:", count)

