from bs4 import BeautifulSoup

def extract_cards(soup):
    page = soup.findAll("td", attrs={"id": "resultsCol"})[0]
    cards = page.findAll("div", attrs={"class": "jobsearch-SerpJobCard unifiedRow row result"})
    return cards
