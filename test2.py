import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

def scrape():
    all_quotes = []
    base_url = "http://quotes.toscrape.com/" #base url that we are going  to scrape
    url = "/page/1" #page1 

    while url:
        res = requests.get(f"{base_url}{url}")
        soup = BeautifulSoup(res.text,"html.parser")
        quotes = soup.find_all(class_ = "quote")
        for quote in quotes:
            all_quotes.append(
                {
                    "text":quote.find(class_="text").get_text(),
                    "author":quote.find(class_="author").get_text(),
                    "bio-link" : quote.find("a")["href"]
                }
            )
        btnnext = soup.find(class_="next")
        if btnnext:
            url = btnnext.find("a")["href"] #Go through the next button field to go to the end of the website to get all the quotes
        else:
            url = None
        sleep(3)
    return all_quotes


def write_quotes_CSV(quotes):
    with open("quotes.csv","w") as file:
        headers = ['text','author','bio-link']
        csv_writer = DictWriter(file,fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)
    print("Quotes written successfully")

all_quotes = scrape()
write_quotes_CSV(all_quotes)
