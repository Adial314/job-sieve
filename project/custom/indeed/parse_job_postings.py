from bs4 import BeautifulSoup
from custom.indeed.call_query import call_query
from custom.indeed.extract_description import extract_description
from custom.indeed.extract_application_link import extract_application_link

def parse_job_postings(cards):
    for card in cards:
        query = card["link"]
        page = call_query(query)

        description = extract_description(page)
        card["description"] = description
        
        try:
            application_link = extract_application_link(page)
        except:
            application_link = query
            
        card["application link"] = application_link
        
    return cards
