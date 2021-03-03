from bs4 import BeautifulSoup

def page_range(page):
    pages = page.findAll("div", attrs={"id": "searchCountPages"})[0].text.strip()
    current_page = int(pages.split()[1])
    final_page = int(pages.split()[3])
    return current_page, final_page
