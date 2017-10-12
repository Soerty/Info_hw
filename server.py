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


@server.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@server.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    result = ''
    for id, keywords in ranging(index, query)[:10]:
        result += '%s</br>%s</br><hr>' % (documents[id].get('title'), documents[id].get('url'))
    return 'Results: \'%s\'' % result



if __name__ == '__main__':
    server.run()