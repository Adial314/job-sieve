from bs4 import BeautifulSoup

def parse_card_location(card):
    div = card.findAll("div", attrs={"class": "sjcl"})[0]
    try:
        location = div.findAll("div", attrs={"class": "location accessible-contrast-color-location"})[0]
    except IndexError:
        location = div.findAll("span", attrs={"class": "location accessible-contrast-color-location"})[0]
    return location.text.strip()
