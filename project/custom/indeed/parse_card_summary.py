from bs4 import BeautifulSoup

def parse_card_summary(card):
    div = card.findAll("div", attrs={"class": "summary"})[0]
    ul = div.findAll("ul", attrs={"style": "list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;"})[0]
    items = ul.findAll("li")

    summary = list()
    for item in items:
        item = item.text.strip()
        summary.append(item)

    return summary
