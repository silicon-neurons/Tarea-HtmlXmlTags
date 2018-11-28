from bs4 import BeautifulSoup, Tag
import requests

html_doc = requests.get("http://www.unitec.edu/")
soup = BeautifulSoup(html_doc.text, "lxml")

for tag in soup.find_all({'script', 'style', 'br'}):
    tag.replaceWith('')

soup = soup.get_text()
soup = BaseException(soup, 'lxml')
print(soup.prettify())
