# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:53:51 2018

@author: VASHIST SINGH
"""
from nltk.corpus import wordnet

synonyms = []
antonymns = []

for syn in wordnet.synsets('good'):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonymns.append(a.name())


print(set(synonyms))
print(set(antonymns))