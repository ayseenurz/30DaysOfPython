"""
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

class Student(Person):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
"""


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        total = 0
        for i in self.data:
            total += i
        return total

    def min(self):
        min_el = self.data[0]
        for i in self.data:
            if i < min_el:
                min_el = i
        return min_el

    def max(self):
        max_el = self.data[0]
        for i in self.data:
            if i > max_el:
                max_el = i
        return max_el

    def range(self):
        rng = self.max() - self.min()
        return rng

    def mean(self):
        sums = self.sum()
        ort = sums / len(self.data)
        return ort

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            medi = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            medi = sorted_data[n // 2]
        return medi

    def mode(self):
        max_count = 0
        mode_value = None
        for i in self.data:
            count = self.data.count(i)
            if count > max_count:
                max_count = count
                mode_value = i
        return (mode_value, max_count)

    def std(self):
        return self.var() ** 0.5

    def var(self):
        avg = self.mean()
        total = 0

        for i in self.data:
            total += (i - avg) ** 2

        return total / len(self.data)

    def freq_dist(self):
        frequencies = {}

        for i in self.data:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1

        return sorted(frequencies.items(), key=lambda item: item[1], reverse = True)


ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]

stats = Statistics(ages)

how_many = stats.count()
print(how_many)

sum_of = stats.sum()
print(sum_of)

min_eleman = stats.min()
print(min_eleman)

max_eleman = stats.max()
print(max_eleman)

rng_lst = stats.range()
print(rng_lst)

ortalama = stats.mean()
print(ortalama)

medi_el = stats.median()
print(medi_el)

mode_lst = stats.mode()
print(mode_lst)

var_lst = stats.var()
print(var_lst)

std_lst = stats.std()
print(std_lst)

freq = stats.freq_dist()
print(freq)

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()

    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income[0]
        return total

    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense[0]
        return total

    def account_info(self):
        return (
            f"Account Holder: {self.firstname} {self.lastname}\n"
            f"Total Income: {self.total_income()}\n"
            f"Total Expense: {self.total_expense()}\n"
            f"Account Balance: {self.account_balance()}"
        )

    def add_income(self, amount, description):
        self.incomes.add((amount, description))

    def add_expense(self, amount, description):
        self.expenses.add((amount, description))

    def account_balance(self):
        return self.total_income() - self.total_expense()


person = PersonAccount("Ayşe", "Yılmaz")

person.add_income(15000, "Monthly salary")
person.add_income(2000, "Freelance work")

person.add_expense(3000, "Rent")
person.add_expense(1000, "Groceries")
person.add_expense(500, "Transportation")

print(person.account_info())