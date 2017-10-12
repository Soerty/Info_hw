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