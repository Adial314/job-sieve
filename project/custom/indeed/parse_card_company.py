from bs4 import BeautifulSoup

def parse_card_company(card):
    div = card.findAll("div", attrs={"class": "sjcl"})[0]
    company = div.findAll("span", attrs={"class": "company"})[0]
    return company.text.strip()
