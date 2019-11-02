from bs4 import BeautifulSoup
import requests
import sys

def get_pages(url, n_pages):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'})
    
    
    print('''
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
        <style>
         figure {
             display: table;
             text-align: center;
             text-indent: 0;
             border: thin silver solid;
             margin: 0.5em;
             padding: 0.5em;
         }

         figcaption {
             display: table-caption;
             caption-side: top;
             font-size: 2em;
         }
        </style>
    </head>
    <body>
''')
    cnt = 0
    
    while cnt < n_pages:
        page = session.get(url)
        ptext = page.text
        soup = BeautifulSoup(ptext)
        
        for l in soup.find_all('a'):
             lnk = l.get('href')
             if lnk and "count=" in lnk: # the "next ›" href contains the text "count=" and "after=", save that link
                 url = lnk
             if lnk and l.text and ('png' in lnk or 'jpg' in lnk): # summarize only images
                 print('''
<figure>
  <img src="%s"/>
  <figcaption>%s</figcaption>
</figure>''' % (lnk, l.text))
        cnt += 1
        
    print('''
    </body>
</html>
''')

if __name__ == "__main__":
    n_pages = 1
    url = "https://old.reddit.com/r/ProgrammerHumor/new/"
    if len(sys.argv) > 1:
        try:
            n_pages = int(sys.argv[1])
        except:
            pass
    if len(sys.argv) > 2:
        url = sys.argv[2]
        
    get_pages(url, n_pages)
        
