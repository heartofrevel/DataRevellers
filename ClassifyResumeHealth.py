# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:41:17 2019

@author: 10060638(heartofrevel)
"""

import os
import pandas as pd
from Utilities import Readers
from Utilities import TextCleaner
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


document_list_resume = []
document_list_health = []


for path, subdirs, files in os.walk(r"C:\Users\10060638\Documents\MLRepository\RESUME"): 
    for name in files:
        # For each file we find, we need to ensure it is a .docx file before adding
        #  it to our list
        if os.path.splitext(os.path.join(path, name))[1] == ".docx":
            document_list_resume.append(os.path.join(path, name))

for path, subdirs, files in os.walk(r"C:\Users\10060638\Documents\MLRepository\HEALTH_TEST"): 
    for name in files:
        # For each file we find, we need to ensure it is a .docx file before adding
        #  it to our list
        if os.path.splitext(os.path.join(path, name))[1] == ".doc":
            document_list_health.append(os.path.join(path, name))

columns = ['CATEGORY', 'DOCUMENT']            

df = pd.DataFrame(columns=columns)

for path in document_list_resume:
    text = Readers.read_docx_file(path).rstrip().strip()
    df = df.append({'CATEGORY':'RESUME', 'DOCUMENT' : text}, ignore_index=True)
    
for path in document_list_health:
    text = Readers.read_doc_file(path).rstrip().strip()
    df = df.append({'CATEGORY':'HEALTH', 'DOCUMENT' : text}, ignore_index=True)
    
of = df
#df['DOCUMENT'] = df['DOCUMENT'].apply(text_process)

bow_transformer = CountVectorizer(analyzer=TextCleaner.text_process).fit(df['DOCUMENT'])
doc_bow = bow_transformer.transform(df['DOCUMENT'])
tfidf_transformer = TfidfTransformer().fit(doc_bow)
doc_tfidf = tfidf_transformer.transform(doc_bow)
doc_classify_model = MultinomialNB().fit(doc_tfidf, df['CATEGORY'])

all_predictions = doc_classify_model.predict(doc_tfidf)
print (classification_report(df['CATEGORY'], all_predictions))


#TIll now we have only predictied on our training data set

#Lets seprate training and test data and try again
from sklearn.model_selection import train_test_split

doc_train, doc_test, cat_train, cat_test = train_test_split(df['DOCUMENT'], df['CATEGORY'], test_size=0.3)

from sklearn.pipeline import Pipeline

#All Steps between line 51 and 55 are done in sindle line.
pipeline = Pipeline([('bow', CountVectorizer(analyzer=TextCleaner.text_process)),('tfidf', TfidfTransformer()), ('classifier', MultinomialNB())])
pipeline.fit(doc_train, cat_train)

predictions = pipeline.predict(doc_test)
print(classification_report(predictions,cat_test))