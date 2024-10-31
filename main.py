# Словарь
books = [
    {'title': 'Война и мир', 'author': 'Лев Толстой', 'year': '1985'},
    {'title': 'Дом в котором', 'author': 'Мариам Петросян', 'year': '1583'},
    {'title': '1984', 'author': 'Джордж Оруэлл', 'year': '1967'},
    {'title': 'Гарри Поттер и философский камень', 'author': 'Дж. К. Роулинг', 'year': '1987'},
    {'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'year': '1887'},
]

# Перебор всех книг и вывод информации
for index in range(len(books)):
    print(f"**Книга {index + 1}***")
    print(f"Название: {books[index]['title']}, Автор: {books[index]['author']}")
    print(f"*** {books[index]['year']}***")
    print()
