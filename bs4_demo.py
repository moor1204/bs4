from bs4 import BeautifulSoup
soup = BeautifulSoup(open("pyladies_wiki.html"))
soup.prettify()

print(soup.title)

print(soup.get_text())

for link in soup.find_all('a'):
    print(link.get('href'))
