import csv
from jinja2 import Template

with open("task3_template.html", "r", encoding="utf-8") as file:
    template = Template(file.read())

def load_books(language):
    books = []
    with open("books.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Язык"].strip().lower() == language.lower():
                books.append(row["Название книги"])
    return books

language = input("Введите язык: ")

books = load_books(language)
html_content = template.render(language=language[:-2] + "ом", books=books)

with open("books_output.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML-страница создана: books_output.html")
