import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv
from datetime import date


class CrawledArticle:
    def __init__(self, title, price, content, image):
        self.title = title
        self.price = price
        self.content = content
        self.image = image


class NetcupCrawler:
    def fetch(self):
        url = "https://www.netcup-sonderangebote.de/"
        time.sleep(1)
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")

        articles = []
        for card in doc.select(".card--inner"):
            price = card.select_one(".card--content--title").select_one("span").text
            title = card.select_one(".card--content--title").text.replace(price, "")
            content = ""
            image = urljoin(url, card.select_one("img").attrs["src"])

            crawled = CrawledArticle(title, price, content, image)
            articles.append(crawled)
        return articles

    def printArticles(self):
        articles = self.fetch()
        for article in articles:
            print("")
            print("Angebot: " + article.title)
            print("         " + article.price)

    def save(self, entries):
        with open("entries.csv", mode="w", newline='') as file:
            fieldnames = ["date", "title", "price"]
            writer = csv.writer(file, delimiter=',', quotechar='"')
            #writer.writeheader()
            for entry in entries:
                writer.writerow([str(date.today()), entry.title, entry.price])

    def check(self, entries):
        with open("entries.csv", mode="r") as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                for entry in entries:
                    if entry.title not in row:
                        return True
            return False
