#декоратор
def select(input_func):    
    def output_func(index): 
        print(f"********Книга {index + 1}*********")  # выводим номер книги
        input_func(index)  
        print(f"********{books['year'][index]}*********")  # выводим год
    return output_func  # возвращаем новую функцию

#списки для словаря 
title = ['Война и мир', 'Дом, в котором', '1984', 'Гарри Поттер и философский камень', 'Мастер и Маргарита']
author = ['Лев Толстой', 'Мариам Петросян', 'Джордж Оруэлл', 'Дж.К. Роулинг', 'Михаил Булгаков']
year = ['1985', '1573', '2145', '4525', '1998']

#Словарь
books = {'title': title, 'author': author, 'year': year}

# перебор все книги и использеум декоратор
for index in range(len(title)):
    @select
    def output(index): 
        print(f"Название книги: {books['title'][index]}, Автор: {books['author'][index]}")

    output(index) 
