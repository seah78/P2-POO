from bs4 import BeautifulSoup
from request import request
from book import Book

BASE_DIR = "http://books.toscrape.com/"


class Category:
    def __init__(self, url):
        self.url = url
        self.url_books = []

    def book_list(self, soup):
        h3s = soup.findAll("h3")
        url_book_list = []
        for h3 in h3s:
            link = h3.find("a")["href"].replace("../../..", BASE_DIR + "catalogue")
            url_book_list.append(link)
        return url_book_list


    def scrape_category(self):
        url_base = self.url
        html = request(self.url)
        soup = BeautifulSoup(html, "html.parser")
        self.url_books.extend(self.book_list(soup))
        if len(self.url_books) == 20:
            page_next = soup.find("ul", "pager").find("li", "next")
            page_number = 1
            while page_next:
                page_number += 1
                page_url = url_base.replace("index.html", f"page-{page_number}.html")
                html = request(page_url)
                soup = BeautifulSoup(html, "html.parser")
                self.url_books.extend(self.book_list(soup))
                page_next = soup.find("ul", "pager").find("li", "next")

    def print_category(self):
        for url in self.url_books:
            thebook = Book(url)
            thebook.scrape_book()
            thebook.print_book()
            print("-------------------------------------------------------------")


category = Category("http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
category.scrape_category()
category.print_category()