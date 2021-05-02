#! /usr/bin/env python3
# coding: utf-8

from bs4 import BeautifulSoup
from request import request

BASE_DIR = "http://books.toscrape.com/"

class Book:
    def __init__(self, url):
        self.product_page_url = url
        self.upc = ""
        self.title = ""
        self.price_including_tax = ""
        self.price_excluding_tax = ""
        self.number_available = ""
        self.product_description = ""
        self.category = ""
        self.review_rating = ""
        self.image_url = ""

    def book_description(self, description):
        if description:
            description = description.text
        else:
            description = ""
        return description

    def book_information(self, trs):
        sub_book = {}
        for tr in trs:
            th = tr.find("th").text
            td = tr.find("td").text
            sub_book[th] = td
        return sub_book

    def scrape_book(self):
        soup = BeautifulSoup(request(self.product_page_url), "html.parser")
        information = self.book_information(soup.findAll("tr"))
        self.upc = information["UPC"]
        self.title = soup.find("article", "product_page").h1.text
        self.price_including_tax = information["Price (incl. tax)"]
        self.price_excluding_tax = information["Price (excl. tax)"]
        self.number_available = information["Availability"]
        self.product_description = self.book_description(soup.find("article").find("p", recursive=False))
        self.category = soup.ul.find_all("a")[-1].text
        self.review_rating = information["Number of reviews"]
        self.image_url = soup.find("img")["src"].replace("../../", BASE_DIR)

    def print_book(self):
        print(f"Title : {self.title}")
        print(f"UPC : {self.upc}")
        print(f"Price inclunding tax : {self.price_including_tax}")
        print(f"Price excluding tax : {self.price_excluding_tax}")
        print(f"Number available : {self.number_available}")
        print(f"Description : {self.product_description}")
        print(f"Category : {self.category}")
        print(f"Number of reviews : {self.review_rating}")
        print(f"Image url : {self.image_url}")


        
