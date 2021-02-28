from bs4 import BeautifulSoup

def extract_application_link(page):
    apply_button = page.findAll("a", attrs={"class": "icl-Button icl-Button--primary icl-Button--md icl-Button--block"})[0]
    application_link = apply_button.get('href')
    return application_link
