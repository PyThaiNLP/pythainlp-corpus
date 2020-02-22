"""
Build PyThaiNLP Corpus WebSite
"""
import os
import sys
import requests
from jinja2 import Environment, FileSystemLoader

json_db_url = 'https://github.com/PyThaiNLP/pythainlp-corpus/raw/2.1/db.json'

r = requests.get(json_db_url)

if r.status_code != 200:
    sys.exit(0)

db = r.json()

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
    filename = os.path.join(root, 'html', str(corpus['name']) + '.html')
    with open(filename, 'w', encoding = 'utf-8') as fh:
        fh.write(template.render(corpus = corpus))