import random
import string

def random_user_id():
    user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return user_id
random_id = random_user_id()
print("Random user ID:", random_id)

def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
        user_ids.append(user_id)
    return user_ids
user_ids = user_id_gen_by_user()
print("Generated user IDs:", user_ids)

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"
random_color = rgb_color_gen()
print("Random RGB color:", random_color)

def list_of_hexa_colors(num):
    hexa_colors = []
    for _ in range(num):
        color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
        hexa_colors.append(color)
    return hexa_colors
num_colors = int(input("Enter the number of hexadecimal colors to generate: "))
hexa_colors = list_of_hexa_colors(num_colors)
print("List of hexadecimal colors:", hexa_colors)

def list_of_rgb_colors(num):
    rgb_colors = []
    for _ in range(num):
        color = rgb_color_gen()
        rgb_colors.append(color)
    return rgb_colors
num_colors = int(input("Enter the number of RGB colors to generate: "))
rgb_colors = list_of_rgb_colors(num_colors)
print("List of RGB colors:", rgb_colors)

def generate_colors(type=None, num_colors=1):
    if type is None:
        color_type = input("Enter the type of colors to generate (hexa/rgb): ").strip().lower()
    else:
        color_type = type

    if num_colors == 1:
        num_colors = int(input("Enter the number of colors to generate: "))

    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
generated_colors = generate_colors()
print("Generated colors:", generated_colors)

lst = [1, 2, 3, 4, 5]

def shuffle_list(lst):
    random.shuffle(lst)
    return lst
shuffled_lst = shuffle_list(lst)
print("Shuffled list:", shuffled_lst)

def random_7_num_in_0_to_9():
    return random.sample(range(10), 7)
random_numbers = random_7_num_in_0_to_9()
print("Random 7 numbers in the range 0-9:", random_numbers)

