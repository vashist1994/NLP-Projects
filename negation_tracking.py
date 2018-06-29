# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:02:43 2018

@author: VASHIST SINGH
"""
import nltk
from nltk.corpus import wordnet
sentence = 'I was not happy with teams performance'

words = nltk.word_tokenize(sentence)

new_word =[]

temp_word = " "

for word in words:
    antonyms =[]
    if word == 'not':
        temp_word = "not_"
    elif temp_word == "not_":
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
    if len(antonyms)>=1:
       word = antonyms[0]
    else:
        word = temp_word + word
        temp_word = ""                
    if word!='not':
        new_word.append(word)
        
sentence = ' '.join(new_word)