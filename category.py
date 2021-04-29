from bs4 import BeautifulSoup
from request import request

BASE_DIR = "http://books.toscrape.com/"


class Category:
	def __init__(self, url):
		self.url = url
		self.url_books = []

	def book_list(soup):
	    h3s = soup.findAll("h3")
	    url_book_list = []
	    for h3 in h3s:
	        link = h3.find("a")["href"].replace("../../..", BASE_DIR + "catalogue")
	        url_book_list.append(link)
	    return url_book_list


	def scrape_category(url):
	    url_base = url
	    html = request(url_base)
	    soup = BeautifulSoup(html, "html.parser")
	    all_book_list = []
	    all_book_list.extend(book_list(soup))
	    if len(all_book_list) == 20:
	        page_next = soup.find("ul", "pager").find("li", "next")
	        page_number = 1
	        while page_next:
	            page_number += 1
	            page_url = url_base.replace("index.html", f"page-{page_number}.html")
	            html = request(page_url)
	            soup = BeautifulSoup(html, "html.parser")
	            all_book_list.extend(book_list(soup))
	            page_next = soup.find("ul", "pager").find("li", "next")
	    return all_book_list