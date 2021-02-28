from bs4 import BeautifulSoup

def parse_card_link(card):
    link = "https://www.indeed.com"
    h2 = card.findAll("h2", attrs={"class": "title"})[0]
    title = h2.findAll("a", attrs={"class": "jobtitle turnstileLink"})[0]
    suffix = title.get('href')
    return link + suffix
