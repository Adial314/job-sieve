from bs4 import BeautifulSoup

def extract_description(page):
    
    try:
        raw_description = page.findAll("div", attrs={"class": "jobsearch-JobComponent-description icl-u-xs-mt--md"})[0]
    except IndexError:
        raw_description = "NO DIV{CLASS: jobsearch-JobComponent-description icl-u-xs-mt--md}"
    except:
        raw_description = "UNSPECIFIED ERROR"
    
    description = raw_description.text.strip()
    return description
