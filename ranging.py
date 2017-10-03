#-*- coding: utf-8 -*-
import os

from reverse_index import reverse_index
from serialization import deserialization_of_article


def set_of_documents():
    documents = []

    for fname in os.listdir('./articles'):
        document = open(os.path.join('./articles', fname)).read()
        documents.append(deserialization_of_article(document))

    return documents



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
    print (reverse_index([i.get('text') for i in documents]))