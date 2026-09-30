dog = {}
print(type(dog))
dog["name"] = "Buddy"
dog["age"] = 5
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
print(dog)

student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "JavaScript", "HTML", "CSS"],
    "country": "USA",
    "city": "New York",
    "address": {
        "street": "123 Main St",
        "zip_code": "10001"
    }
}
print(len(student))
print(student["skills"])
student["skills"].append("SQL")
print(student["skills"])

keys = student.keys()
print(keys)
values = student.values()
print(values)

student_items = student.items()
print(student_items)

del student["marital_status"]
print(student)

del dog