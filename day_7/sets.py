# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("the lenght of the set:",len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["Tiktok", "Snapchat", "Reddit"])
print(it_companies)

it_companies.remove("Tiktok")
print(it_companies)

it_companies.discard("Snapchat")
print(it_companies)
#it_companies.remove("Snapchat") # This will raise a KeyError since "Snapchat" has already been removed
#print(it_companies)

a_b = A.union(B)
print(a_b)

a_b_intersection = A.intersection(B)
print(a_b_intersection)

print(A.issubset(B))

a_b_isdisjoint = A.isdisjoint(B)
print(a_b_isdisjoint)

a_join_b = A.union(B)
print(a_join_b)
b_join_a = B.union(A)
print(b_join_a)

a_b_symmetric_difference = A.symmetric_difference(B)
print(a_b_symmetric_difference)

del a_b, a_b_intersection, a_b_isdisjoint, a_join_b, b_join_a, a_b_symmetric_difference

print(len(age))
age_lt = list(age)
print(len(age_lt))

#the difference between string, list, tuple set is that string, 
#list and tuple are ordered collection of items 
#but set is unordered collection of unique items.

some_sentence = "I am a teacher and I love to inspire and teach people"
words = some_sentence.split()
unique_words = set(words)
print(unique_words)