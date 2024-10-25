import random
import datetime
from jinja2 import Template

with open("task2_template.txt", "r", encoding="utf-8") as file:
    template = Template(file.read())

def generate_login(name):
    initials = "".join([word[0] for word in name.split()])
    return f"{initials}_{name.split()[-1].lower()}"

def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(10))

def get_time_of_day():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    elif 18 <= hour < 22:
        return "evening"
    else:
        return "night"

name = input("Введите имя: ")
preferred_language = input("Предпочитаемый язык: ").lower()

available_languages = ["русский", "английский", "немецкий", "французский", "древнерусский"]
if preferred_language in available_languages:
    language = preferred_language
else:
    language = "русский"

data = {
    "name": name,
    "time_of_day": get_time_of_day(),
    "language": language,
    "login": generate_login(name),
    "password": generate_password()
}

output = template.render(data)
print(output)
