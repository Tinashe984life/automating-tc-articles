from bs4 import BeautifulSoup
from colorama import Fore
import requests

links = []

class Article:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return (f'Article Name: {self.name} \n Article URL: {self.url}')

def getLinks():
    html_text = requests.get('https://techcrunch.com/').text
    bs = BeautifulSoup(html_text, 'lxml')
    container = bs.find('div', class_='river river--homepage')
    #print(Fore.RED, container)
    articles = container.find_all('a', class_='post-block__title__link')
    for article in articles:    
        articleName = article.text.strip()
        articleUrl = article.attrs['href']
        newArticle = Article(articleName, articleUrl)
        links.append(newArticle)
        #print(Fore.GREEN, f'Article: {articleName} \n {Fore.YELLOW}URL: {articleUrl}')
        
    print(Fore.GREEN, 'Articles Successfully collected')

getLinks()