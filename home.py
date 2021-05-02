from bs4 import BeautifulSoup
from request import request
from category import Category

BASE_DIR = "http://books.toscrape.com/"

class Home:
    def __init__(self, url):
        self.url = url
        self.url_category = []

    def scrape_home(self):
        html = request(self.url)
        soup = BeautifulSoup(html, "html.parser")
        lis = soup.find("ul", {"class": "nav nav-list"}).find("ul").findAll("li")
        for li in lis:
            link = BASE_DIR + li.find("a")["href"]
            self.url_category.append(link)


    def print_home(self):
        for url in self.url_category:
            thecategory = Category(url)
            thecategory.scrape_category()
            thecategory.print_category()
            print("****************************************************************")
        
