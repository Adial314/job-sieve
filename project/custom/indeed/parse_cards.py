from custom.indeed.parse_card_title import parse_card_title
from custom.indeed.parse_card_link import parse_card_link
from custom.indeed.parse_card_company import parse_card_company
from custom.indeed.parse_card_location import parse_card_location
from custom.indeed.parse_card_summary import parse_card_summary

def parse_cards(cards):
    
    parsed_cards = list()
    for card in cards:
        
        # Parse attributes
        parsed_cards.append(dict({
            "title": parse_card_title(card),
            "link": parse_card_link(card),
            "company": parse_card_company(card),
            "location": parse_card_location(card),
            "summary": parse_card_summary(card)
        }))
        
    return parsed_cards
