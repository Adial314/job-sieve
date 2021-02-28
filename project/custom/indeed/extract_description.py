from bs4 import BeautifulSoup

def extract_description(page):
    raw_description = page.findAll("div", attrs={"class": "jobsearch-JobComponent-description icl-u-xs-mt--md"})[0]
    description = raw_description.text.strip()
    return description
