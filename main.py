#списки для словаря 
title = ['Война и мир', 'Дом, в котором', '1984', 'Гарри Поттер и философский камень', 'Мастер и Маргарита']
author = ['Лев Толстой', 'Мариам Петросян', 'Джордж Оруэлл', 'Дж.К. Роулинг', 'Михаил Булгаков']
year = ['1985', '1573', '2145', '4525', '1998']

#Словарь
books = {'title': title, 'author': author, 'year': year}

# перебор все книги и использеум 
for index in range(len(title)):
    print(f"********Книга {index + 1}*********")
    print(f"Название:{books['title'][index]},Автор: {books['author'][index]}")
    print(f"********{books['year'][index]}*********")  # выводим год
    print()
