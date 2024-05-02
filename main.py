# Є словник з друзями, де ключ – людина, а значення –
# список друзів. Користувач вводить імена двох людей,
# які є друзями, повторює це певну кількість разів,
# після чого дані зберігаються у файл.
# Завантажте дані назад та виведіть на екран.
import json


def load_friends():
    try:
        with open("friends_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_friends(friends_dict):
    with open("friends_data.json", "w") as file:
        json.dump(friends_dict, file)


def add_friendship(friends_dict, person1, person2):
    if person1 not in friends_dict:
        friends_dict[person1] = [person2]
    else:
        friends_dict[person1].append(person2)

    if person2 not in friends_dict:
        friends_dict[person2] = [person1]
    else:
        friends_dict[person2].append(person1)


def print_friends(friends_dict):
    for person, friends_list in friends_dict.items():
        print(f"{person} має друзів: {', '.join(friends_list)}")


friends_dict = load_friends()

num = int(input("Введіть кількість друзів, щоб додати/оновити: "))

for _ in range(num):
    person1 = input("Введіть ім'я першої особи: ")
    person2 = input("Введіть ім'я другої особи: ")
    add_friendship(friends_dict, person1, person2)

save_friends(friends_dict)


print("Дані про дружбу:")
print_friends(friends_dict)




