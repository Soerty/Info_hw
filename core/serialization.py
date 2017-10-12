#-*- coding: utf-8 -*-
import uuid


def serialization_of_article(article):
    fname = '%s.txt' % uuid.uuid4()
    content = "@author {author}\n@title {title}\n@date {date}\n@url {url}\n{text}".format(**article)
    with open('./articles/%s' % fname, 'a') as file:
        file.write(content)


def deserialization_of_article(content):
    article = {}

    lines = content.split('\n')
    article['author'] = lines.pop(0)[8:]
    article['title'] = lines.pop(0)[7:]
    article['date'] = lines.pop(0)[6:]
    article['url'] = lines.pop(0)[5:]
    article['text'] = lines.pop(0)

    return article