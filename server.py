#-*- coding: utf-8 -*-
#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import render_template

from core.reverse_index import reverse_index
from core.ranging import set_of_documents
from core.ranging import ranging

server = Flask(__name__)
documents = set_of_documents()
index = reverse_index([i.get('text') for i in documents])

@server.template_filter('shorten')
def shorten(string):
    return string if len(string) < 60 else string[:60] + '...'

server.jinja_env.filters['shorten'] = shorten



@server.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@server.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form['query']

    results = []
    for id, keywords in ranging(index, query):
        results.append((documents[id].get('title'), documents[id].get('url')))

    return render_template('search.html', search_query=query, searching_results=results)



if __name__ == '__main__':
    server.run()