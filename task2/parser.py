import sys
from bs4 import BeautifulSoup as Soup
from ebooklib import epub

# Добавляем в список названия книг из консоли
books = [line.strip() for line in sys.stdin]

for book_name in books:
    '''Перебираем названия книг и если проходят по формату .fb2, то через библиотеку BeautifulSoap достаем необходимую информацию'''

    if book_name.endswith('.fb2'):
        with open(book_name, encoding='utf-8') as xml:
            soup = Soup(xml.read(), features="lxml")
            print(
                f"{soup.find('book-title', ).text}, {soup.find('first-name', ).text}, {soup.find('middle-name', ).text}, {soup.find('last-name', ).text}, {soup.find('publisher', ).text}, {soup.find('year', ).text}")

    elif book_name.endswith('.epub'):
        # В случае формата .epub через библиотеку epub достаем необходимую информацию
        book = epub.read_epub(book_name)

        #Проверка на существование заданной инормации
        try:
            title = book.get_metadata('DC', 'title')[0][0]
        except IndexError:
            title = 'Не указан'
        try:
            creator = book.get_metadata('DC', 'creator')[0][0]
        except IndexError:
            creator = 'Не указан'
        try:
            publisher = book.get_metadata('DC', 'publisher')[0][0]
        except IndexError:
            publisher = 'Не указан'
        try:
            publish_year = book.get_metadata('DC', 'date')[0][0][:4]
        except IndexError:
            publish_year = 'Не указан'

        print(
            f"{title}, {creator}, {publisher}, {publish_year}")

    else:
        print('Нет книг формата .fb2 или .epub')
