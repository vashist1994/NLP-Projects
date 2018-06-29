# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:41:41 2018

@author: VASHIST SINGH
"""
import numpy as np
import nltk
import pickle
import re
from nltk.corpus import stopwords
from sklearn.datasets import load_files
nltk.download('stopwords')


#importing datasets
reviews = load_files('txt_sentoken/')

x,y = reviews['data'],reviews['target']


#storing
with open('x.pickle','wb') as f:
    pickle.dump(x,f)
    
with open('y.pickle','wb') as f:
    pickle.dump(y,f)
    
#reading
    with open('x.pickle','rb')as f:
        x = pickle.load(f)
    with open('y.pickle','rb')as f:
        y = pickle.load(f)

#creating the corpus of processed data

corpus = []

for i in range(0, len(x)):
    review = re.sub(r'\W', ' ', str(x[i]))
    review = review.lower()
    review = re.sub(r'^br$', ' ', review)
    review = re.sub(r'\s+br\s+',' ',review)
    review = re.sub(r'\s+[a-z]\s+', ' ',review)
    review = re.sub(r'^b\s+', '', review)
    review = re.sub(r'\s+', ' ', review)
    corpus.append(review)

#creating the Bag of word model
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features=2000,min_df=3,max_df=0.6,stop_words=stopwords.words('english')) 

x = vectorizer.fit_transform(corpus).toarray()

#converting Bag into tfidf model
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
x= transformer.fit_transform(x).toarray()

#creating the TFIDF model

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=2000,min_df=3,max_df=0.6,stop_words=stopwords.words('english')) 

x = vectorizer.fit_transform(corpus).toarray()

#splitting the model
from sklearn.model_selection import train_test_split
text_train,text_test,sent_train,sent_test = train_test_split(x,y,test_size=0.2,random_state=0)

#Machine learning part
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

#Training the model
model.fit(text_train,sent_train)

#predicting the test set result

predict = model.predict(text_test)

#performance measure
from sklearn.metrics import classification_report,confusion_matrix
c_report = classification_report(sent_test,predict)
c_metrix = confusion_matrix(sent_test,predict)

#Storing the model

with open('classifier.pickle','wb') as f:
    pickle.dump(model,f)

#storing the vectorizer
with open('tfidfmodel.pickle','wb') as f:
    pickle.dump(vectorizer,f)
        
 
#reading the classifier and vectorizer
with open('classifier.pickle','rb') as f:
    clf = pickle.load(f)
    
with open('tfidfmodel.pickle','rb') as f:
    tfidf = pickle.load(f)  


sample = ["you are a bad Person man, have a worst life"]
sample = tfidf.transform(sample).toarray()

print(clf.predict(sample))
        
        
        