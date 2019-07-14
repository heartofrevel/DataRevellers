# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 11:25:37 2019

@author: 10060638
"""



from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer


def text_process(text):

    text = re.sub('\s+',' ', text)
    
    text_words = word_tokenize(text)
    # Check characters to see if they are in punctuation
    #ps = PorterStemmer() 
    wordnet_lemmatizer = WordNetLemmatizer()
    punctuations="?:!.,;"
    for index, word in enumerate(text_words):
        if word in punctuations:
            text_words.remove(word)
        elif word.lower() in stopwords.words('english'):
            text_words.remove(word)
        else:
            #word = wn._morphy(word, wn.NOUN)
            text_words[index] = wordnet_lemmatizer.lemmatize(word, pos='v')
             
    return text_words