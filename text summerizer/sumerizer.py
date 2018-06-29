# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:46:53 2018

@author: VASHIST SINGH
"""

import bs4 as bs
import urllib.request
import re
import nltk
nltk.download('stopwords')
import heapq

#getting the data

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

soup = bs.BeautifulSoup(source,'lxml')

text = ""
for paragraph in soup.find_all('p'):
    text +=paragraph.text
    
#preprocessing the txt
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
clean_text = text.lower()
clean_text = re.sub(r'\W',' ',clean_text)
clean_text = re.sub(r'\d',' ',clean_text)
clean_text = re.sub(r'\s+',' ',clean_text)

#Tokenizing the Article
sentences = nltk.sent_tokenize(text)
stopwords = nltk.corpus.stopwords.words('english')

#Besic histogram
word2count = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stopwords:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] +=1

#weughted histogram
            
for key in word2count.keys():
    word2count[key] = word2count[key]/max(word2count.values())
    
    
#finding the score
    
sentence2score = {}
for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if len(sentence.split(' ')) < 25:
            if word in word2count.keys():
                if sentence not in sentence2score.keys():
                    sentence2score[sentence]= word2count[word]
                else:
                    sentence2score[sentence] += word2count[word]
                    
#getting the summery
best_sentences=heapq.nlargest(5,sentence2score,key=sentence2score.get)

print('----------------------------------------------------------------------------')

for sentences in best_sentences:
    print(sentences)