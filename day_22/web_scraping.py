import requests
import pandas as pd
import json
from io import StringIO
from bs4 import BeautifulSoup

url = "https://www.bu.edu/president/boston-university-facts-stats/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

data = {
    "title": "",
    "headings": [],
    "paragraphs": [],
    "tables": []
}

if soup.title:
    data["title"] = soup.title.get_text(strip=True)

for heading in soup.find_all(["h1", "h2", "h3", "h4"]):
    text = heading.get_text(" ", strip=True)

    if text:
        data["headings"].append({
            "tag": heading.name,
            "text": text
        })

for paragraph in soup.find_all("p"):
    text = paragraph.get_text(" ", strip=True)

    if text:
        data["paragraphs"].append(text)

for table in soup.find_all("table"):
    rows = []

    for tr in table.find_all("tr"):
        cells = tr.find_all(["th", "td"])

        row = [
            cell.get_text(" ", strip=True)
            for cell in cells
        ]

        if row:
            rows.append(row)

    if rows:
        data["tables"].append(rows)

with open("boston_university.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Veriler boston_university.json dosyasına kaydedildi.")
print("Başlık sayısı:", len(data["headings"]))
print("Paragraf sayısı:", len(data["paragraphs"]))
print("Tablo sayısı:", len(data["tables"]))

url = "https://archive.ics.uci.edu/ml/datasets"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

print("İstek yapılan adres:", response.url)
print("HTTP durum kodu:", response.status_code)
print("HTML önizlemesi:", response.text[:300])

html = StringIO(response.text)

try:
    tables = pd.read_html(html)
except ValueError:
    tables = []

if tables:
    df = max(tables, key=len)

    df.to_json(
        "uci_datasets.json",
        orient="records",
        force_ascii=False,
        indent=4
    )

    print("Tablo uci_datasets.json dosyasına kaydedildi.")
    print("Satır sayısı:", len(df))

else:
    print("Eski URL'de HTML tablosu bulunamadı.")
    print("Yeni UCI sayfası:", "https://archive.ics.uci.edu/datasets")

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

headers = {
    "User-Agent": "PythonWebScrapingPractice/1.0 (educational project)"
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

tables = pd.read_html(response.text)

print("Bulunan tablo sayısı:", len(tables))

presidents_table = None

for table in tables:
    columns = [
        str(column).lower()
        for column in table.columns
    ]

    if any("president" in column or "name" in column
           for column in columns) and any(
               "term" in column for column in columns
           ):
        presidents_table = table
        break

if presidents_table is None:
    raise ValueError("Başkanlar tablosu bulunamadı.")

if isinstance(presidents_table.columns, pd.MultiIndex):
    presidents_table.columns = [
        " ".join(
            str(part)
            for part in column
            if str(part) != "nan"
        ).strip()
        for column in presidents_table.columns
    ]

presidents_table.columns = [
    str(column).strip()
    for column in presidents_table.columns
]

def clean_value(value):
    if pd.isna(value):
        return None

    if isinstance(value, str):
        return " ".join(value.split())

    return value

presidents_table = presidents_table.map(clean_value)

data = presidents_table.to_dict(orient="records")

with open("us_presidents.json", "w", encoding="utf-8") as file:
    json.dump(
        data,
        file,
        ensure_ascii=False,
        indent=4,
        default=str
    )

print("Veriler us_presidents.json dosyasına kaydedildi.")
print("Başkan tablosundaki satır sayısı:", len(data))

print(json.dumps(data[:3], ensure_ascii=False, indent=4))