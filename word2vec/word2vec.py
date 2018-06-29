# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:43:30 2018

@author: VASHIST SINGH
"""

import bs4 as bs
import re
import urllib.request
import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
nltk.download('stopwords')

source  = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

soup  = bs.BeautifulSoup(source,'lxml')

text=""
for paragraph in soup.find_all('p'):
    text+= paragraph.text
    
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'[@#\$%&\*\(\)\<\>\?\'\":;]\[-]',' ',text)
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)


sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]

model = Word2Vec(sentences,min_count=1)

words = model.wv.vocab

vector = model.wv['global']

similar = model.wv.most_similar('global')