from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl

def call_query(query):
    # For ignoring SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    # Making the website believe that you are accessing it using a Mozilla browser
    req = Request(query, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    # Creating a BeautifulSoup object of the HTML page for easy extraction of data.
    soup = BeautifulSoup(webpage, 'html.parser')
    
    return soup
