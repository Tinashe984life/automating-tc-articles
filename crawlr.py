from bs4 import BeautifulSoup
from colorama import Fore
import requests

links = []

class Article: # Article Class 
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return (f'Article Name: {self.name} \n Article URL: {self.url}')

def getLinks(): # Grabs the latest stories , Headlines + URLs
    html_text = requests.get('https://techcrunch.com/').text
    bs = BeautifulSoup(html_text, 'lxml')
    container = bs.find('div', class_='river river--homepage')
    articles = container.find_all('a', class_='post-block__title__link')
    for article in articles:    
        articleName = article.text.strip()
        articleUrl = article.attrs['href']
        newArticle = Article(articleName, articleUrl)
        links.append(newArticle)
        
    print(Fore.GREEN, 'Articles Successfully collected')

def grabArticle(): # Goes to each article url and grabs the article text 
    for link in links:
        print(Fore.RED, link.name)
        html_text = requests.get(link.url).text
        soup = BeautifulSoup(html_text, 'lxml')
        article = soup.find('div', class_='article-content')
        paragraphs = article.find_all('p')
        for p in paragraphs:
            print(Fore.YELLOW, p.text)

getLinks()
grabArticle()