import re
import keyword

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
paragraph = paragraph.lower()
words = re.findall(r'\b\w+\b', paragraph)
word_dict = {}

for word in words:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

sorted_words = sorted(
    word_dict.items(),
    key=lambda item: item[1],
    reverse=True
)

print(sorted_words)

sentence = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction"

numbers = re.findall(r'-?\d+', sentence)

numbers = list(map(int, numbers))

sorted_numbers = sorted(numbers)

diff = sorted_numbers[-1] - sorted_numbers[0]

print("Numbers:", sorted_numbers)
print("Distance:", diff)

def is_valid_variable(name):
    pattern = r'^[a-zA-Z_]\w*$'

    if re.fullmatch(pattern, name) and not keyword.iskeyword(name):
        return True
    else:
        return False

print(is_valid_variable('first_name'))   
print(is_valid_variable('first-name'))   
print(is_valid_variable('1first_name'))  
print(is_valid_variable('firstname'))    

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()


def most_frequent_words(text):
    words = re.findall(r'\b\w+\b', text)
    word_dict = {}

    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    sorted_words = sorted(
        word_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return [(count, word) for word, count in sorted_words[:3]]

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))