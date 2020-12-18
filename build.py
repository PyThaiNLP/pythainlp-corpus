"""
Build PyThaiNLP Corpus WebSite
"""
import os
import sys
import json
from jinja2 import Environment, FileSystemLoader
from shutil import copyfile
import os

json_db_url = 'db.json'

with open(json_db_url, encoding='utf-8') as fh:
    db = json.load(fh)

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
# index
template = env.get_template('index.html')
filename = os.path.join(root, 'html', 'index.html')
with open(filename, 'w', encoding = 'utf-8') as fh:
    fh.write(template.render())

# List Corpus
list_corpus = list(db.keys())
list_corpus.remove('test') # del test
list_corpus.sort()

listcorpus = [db[i] for i in list_corpus]

template = env.get_template('list-corpus.html')
filename = os.path.join(root, 'html', 'list-corpus.html')
with open(filename, 'w', encoding = 'utf-8') as fh:
    fh.write(template.render(listcorpus = listcorpus))

# details
template = env.get_template('details.html')
for corpus in listcorpus:
    #print(corpus)
    filename = os.path.join(root, 'html', str(corpus['name']) + '.html')
    with open(filename, 'w', encoding = 'utf-8') as fh:
        fh.write(template.render(corpus = corpus))

copyfile(json_db_url, os.path.join('html',json_db_url))