#-*- coding: utf-8 -*-
import os
import uuid
import shutil
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Parser:
    @staticmethod
    def get_newspapers_for_the_year(link):
        soup = BeautifulSoup(urlopen(link).read().decode('utf-8'), "lxml")

        return [
            tag.find('a').get('href') 
                for tag in soup.body.findAll('div', attrs={'class': 'clauses-arhive'})
        ]

    @staticmethod
    def get_articles_from_category(link):
        soup = BeautifulSoup(urlopen(link).read().decode('utf-8'), "lxml")

        return [
            tag.find('a').get('href') 
                for tag in soup.body.findAll('div', attrs={'class': 'clauses-name'})
        ]

    @staticmethod
    def get_article(link):
        soup = BeautifulSoup(urlopen(link).read().decode('utf-8'), "lxml")
        content = soup.body.find('div', attrs={'class': 'clauses-id'})

        article = {}
        article['url'] = link
        article['title'] = content.find('div', attrs={'class': 'clauses-name-id'}).text
        article['author'] = content.find('div', attrs={'class': 'clauses_anons'}).find('p').text
        article['date'] = content.find('div', attrs={'class': 'number_current_id'}).text
        article['text'] = content.find('div', attrs={'class': 'clauses_text'}).text
    
        return article


def serialization_of_articles(articles):
    if os.path.exists('./articles'):
        shutil.rmtree('./articles')
    os.mkdir('./articles')

    for article in articles:
        fname = '%s.txt' % uuid.uuid4()

        content = "@author {author}\n@title {title}\n@date {date}\n@url {url}\n\n{text}".format(**article)
        with open('./articles/%s' % fname, 'a') as file:
            file.write(content)



if __name__ == '__main__':
    limit = 1
    base_url = 'http://www.vecherniyorenburg.ru/year2016/'

    articles = []
    categories = Parser.get_newspapers_for_the_year(base_url)
    while categories and limit:
        category = categories.pop(0)
        for article in Parser.get_articles_from_category(category):
            if limit == 0:
                break
            limit -= 1

            print (article)
            articles.append(Parser.get_article(article))

    serialization_of_articles(articles)