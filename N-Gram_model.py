# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:40:27 2018

@author: VASHIST SINGH
"""

import random

#sample text

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""
n=5
ngrams = {}

for i in range(len(text)-n):
    gram = text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
        ngrams[gram].append(text[i+n])
        
currentgram = text[0:n]
result = currentgram
for i in range(100):
    if currentgram not in ngrams.keys():
        break
    possiblity = ngrams[currentgram]
    nextitem = possiblity[random.randrange(len(possiblity))]
    result +=nextitem
    currentgram = result[len(result)-n:len(result)]

print(result)

len(result)