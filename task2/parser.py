import sys
from bs4 import BeautifulSoup as Soup
from ebooklib import epub

# Добавляем в список названия книг
books = [line.strip() for line in sys.stdin]

for book_name in books:
    '''Перебираем названия книг и если проходят по формату .fb2, то через библиотеку BeautifulSoap достаем необходимую информацию'''
    if book_name.endswith('.fb2'):
        with open(book_name, encoding='utf-8') as xml:
            soup = Soup(xml.read(), features="lxml")
            print(
                f"{soup.find('book-title', ).text}, {soup.find('first-name', ).text}, {soup.find('middle-name', ).text}, {soup.find('last-name', ).text}, {soup.find('publisher', ).text}, {soup.find('year', ).text}")
    else:
        # В ином случае через библиотеку epub достаем необходимую информацию
        book = epub.read_epub(book_name)
        print(
            f"{book.get_metadata('DC', 'title')[0][0]}, {book.get_metadata('DC', 'creator')[0][0]}, {book.get_metadata('DC', 'publisher')[0][0]}, {book.get_metadata('DC', 'date')[0][0][:4]}")
