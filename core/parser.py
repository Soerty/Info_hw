#-*- coding: utf-8 -*-
import os
import shutil
from urllib.request import urlopen

from bs4 import BeautifulSoup

from serialization import serialization_of_article


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
        article['date'] = content.find('div', attrs={'class': 'number_current_id'}).text
        article['text'] = content.find('div', attrs={'class': 'clauses_text'}).text
        author_block = content.find('div', attrs={'class': 'clauses_anons'})#.find('p').text
        article['author'] = author_block.find('p').text if author_block else 'None'
    
        return article



if __name__ == '__main__':
    limit = 50
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

    if os.path.exists('./articles'):
        shutil.rmtree('./articles')
    os.mkdir('./articles')

    for article in articles:
        serialization_of_article(article)