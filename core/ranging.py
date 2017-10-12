#-*- coding: utf-8 -*-
import os
from collections import defaultdict

from .serialization import deserialization_of_article


def set_of_documents():
    documents = []

    for fname in os.listdir('core/articles'):
        document = open(os.path.join('core/articles', fname)).read()
        documents.append(deserialization_of_article(document))

    return documents


def ranging(index, request):
    freq = defaultdict(list)

    for word in request.lower().split():
        for id in index[word]:
            freq[id].append(word)
    
    return sorted(freq.items(), key=lambda v: len(v[1]), reverse=True)


"""
if __name__ == '__main__':
    if not os.path.exists('./articles'):
        print ('There is no collection of documents, please, first run:')
        print ('')
        print ('    $ python3 parser.py')
        print ('')
        print ('And then try again :)')
        print ('')
        print ('    $ python3 ranging.py')
        print ('')
        exit(1)

    request = str(input('Input your search request: '))
    documents = set_of_documents()
    index = reverse_index([i.get('text') for i in documents]) 

    print ('')
    print ('')
    print ('Request:  %s' % request)
    print ('')
    for id, keywords in ranging(index, request)[:10]:
        print ('Keywords: %s' % ', '.join(keywords))
        print ('Title: %s' % documents[id].get('title'))
        print ('URL:  %s' % documents[id].get('url'))
        print ('-' * 80)
        print ('')
"""