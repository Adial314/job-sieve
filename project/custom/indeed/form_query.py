def form_query(keywords, location=None):
    
    base = "https://www.indeed.com/jobs?"
    
    keyword_chain = str()
    for keyword in keywords:
        if len(keyword_chain) == 0:
            keyword_chain += "q=" + keyword
        else:
            keyword_chain += "+" + keyword

    if location:
        location = "&l=" + location
        
    return base + keyword_chain + location
