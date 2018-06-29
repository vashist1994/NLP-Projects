# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 21:21:10 2018

@author: VASHIST SINGH
"""

import tweepy
import re
import pickle
from tweepy import OAuthHandler

#initializing all the keys

cousumer_key = "brPFxhhIYILTu7ftTeGeOXt5Q"
consumer_secret = "2IgvbL56qPmtfyIDLlY48IOIRmtrRj3hRBgmYTs25n7TXqCUed"
access_token = "4580542527-s7esBw9EHAcpC4APn1lcyW7cXxj2GawLRq79HtX"
access_secret = "Jwjb8FXOAYfPCnh7HPrVdRUPfO8cl8uCoEhUybzo3QTI2"  

#setting up the authemtication hamdler

auth = OAuthHandler(cousumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

args = ['google']

api = tweepy.API(auth,timeout=10)

#fetching the tweets related to facebook from twitter

list_tweets = []
query = args[0]
if len(args)==1:
    for status in tweepy.Cursor(api.search,q=query+"-filter:retweets",lang='en',result_type='recent').items(100):
        list_tweets.append(status.text)
        
#loading the pre trained model an Vectorizer
with open('tfidfmodel.pickle','rb') as f:
    vectorizer = pickle.load(f)
    
with open('classifier.pickle','rb') as f:
    clf = pickle.load(f)

total_pos = 0
total_neg = 0

#preprocessing the tweets

for tweet in list_tweets:
    tweet = re.sub(r"^https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*$", " ", tweet)
    tweet = tweet.lower()
    tweet = re.sub(r"that's","that is",tweet)
    tweet = re.sub(r"there's","there is",tweet)
    tweet = re.sub(r"what's","what is",tweet)
    tweet = re.sub(r"where's","where is",tweet)
    tweet = re.sub(r"it's","it is",tweet)
    tweet = re.sub(r"who's","who is",tweet)
    tweet = re.sub(r"i'm","i am",tweet)
    tweet = re.sub(r"she's","she is",tweet)
    tweet = re.sub(r"he's","he is",tweet)
    tweet = re.sub(r"they're","they are",tweet)
    tweet = re.sub(r"who're","who are",tweet)
    tweet = re.sub(r"ain't","am not",tweet)
    tweet = re.sub(r"wouldn't","would not",tweet)
    tweet = re.sub(r"shouldn't","should not",tweet)
    tweet = re.sub(r"can't","can not",tweet)
    tweet = re.sub(r"couldn't","could not",tweet)
    tweet = re.sub(r"won't","will not",tweet)
    tweet = re.sub(r"\W"," ",tweet)
    tweet = re.sub(r"\d"," ",tweet)
    tweet = re.sub(r"\s+[a-z]\s+"," ",tweet)
    tweet = re.sub(r"\s+[a-z]$"," ",tweet)
    tweet = re.sub(r"^[a-z]\s+"," ",tweet)
    tweet = re.sub(r"\s+"," ",tweet)
    sent= clf.predict(vectorizer.transform([tweet]).toarray())
    if sent[0] == 1:
        total_pos +=1
    else:
        total_neg +=1
        

#plotting the bar graph
import matplotlib.pyplot as plt
import numpy as np
objects = ['positive','Negative']
y_pos = np.arange(len(objects))

plt.bar(y_pos,[total_pos,total_neg],alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel('Number')
plt.title('Number of positive and Negative Tweets')
plt.show()
















