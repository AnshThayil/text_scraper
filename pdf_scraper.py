import requests
import sys
import io
import PyPDF2
from bs4 import BeautifulSoup

def encode_url(url):
    return url.replace("/", "-").replace(":", "-").replace("?", "-") + '.txt'

def scrape_text_from_pdf(r):
    fio = io.BytesIO(r.content)
    reader = PyPDF2.PdfReader(fio)
    pages = reader.pages
    text = "".join([page.extract_text() for page in pages])
    return text

def scrape_text_from_html(r):
    soup = BeautifulSoup(r.content, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def scrape_url(url):    
    r = requests.get(url)
    with open(encode_url(url), 'w+') as f:
        content_type = r.headers.get('content-type')
        if 'text/html' in content_type:
            pass
            print("Found HTML File at " + url)
            text = scrape_text_from_html(r)
            f.write(text)

        elif 'application/pdf' in content_type:
            print("Found PDF File at " + url)
            text = scrape_text_from_pdf(r)
            f.write(text)
            


if __name__ == '__main__':

    assert(len(sys.argv) == 3)
    assert(sys.argv[1] == '--url'  or sys.argv[1] == '--txt')

    if sys.argv[1] == '--url':
        scrape_url(sys.argv[2])

    elif sys.argv[1] == '--txt':
        with open(sys.argv[2], 'r') as f:
            for line in f.read().split('\n'):
                scrape_url(line)