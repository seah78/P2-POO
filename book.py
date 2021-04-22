from bs4 import BeautifulSoup
from request import request

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
BASE_DIR = "http://books.toscrape.com/"

class Book:
	def __init__(self, b_url, b_upc, b_title, b_price_including_tax, b_price_excluding_tax, b_number_available, b_product_description, b_category, b_review_rating, b_image_url):
		self.product_page_url = b_url
		self.upc = b_upc
		self.title =b_title
		self.price_including_tax = b_price_including_tax
		self.price_excluding_tax = b_price_excluding_tax
		self.number_available = b_number_available
		self.product_description = b_product_description
		self.category = b_category
		self.review_rating = b_review_rating
		self.image_url = b_image_url


def book_description(description):
    if description:
        description = description.text
    else:
        description = ""
    return description


def book_information(trs):
    sub_book = {}
    for tr in trs:
        th = tr.find("th").text
        td = tr.find("td").text
        sub_book[th] = td
    return sub_book


def scrape_book(url):
    soup = BeautifulSoup(request(url), "html.parser")
    information = book_information(soup.findAll("tr"))
    book = Book(url, information["UPC"], soup.find("article", "product_page").h1.text, information["Price (incl. tax)"], information["Price (excl. tax)"], information["Availability"], book_description(soup.find("article").find("p", recursive=False)), soup.ul.find_all("a")[-1].text, information["Number of reviews"], soup.find("img")["src"].replace("../../", BASE_DIR))
    print(Book)
