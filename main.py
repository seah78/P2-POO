#! /usr/bin/env python3
# coding: utf-8

from home import Home

def main():

	home = Home("http://books.toscrape.com/")
	home.scrape_home()
	home.print_home()

if __name__ == "__main__":
    main()