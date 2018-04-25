# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:15:02 2018

@author: bsuzow
text_processing.py

Tokenize the hearings corpora
Remove stop words
Create wordclouds
ref: https://www.nltk.org/
ref: http://www.nltk.org/book/

"""
import nltk 
from nltk.corpus import stopwords
#from pprint import pprint
import os
# nltk.download('punkt')  # run once
# nltk.download('stopwords')  # run once
# nltk.download()  # took too long. aborted
# os.getcwd()
def Tokenize(text_data,hearing_day):
    """
    Joins the strings in the text_data list to make it a long string obj.
    Tokenizes the string obj.
    Arguments:
        text_data: a list obj of paragraphs scraped from the web
        hearing_day: 1 for the first day; 2 for the 2nd
        
    Return Values:
        1. Sanitized word tokens from text_data in a list object of strings/words
        2. Word tokens frequency distribution (FreqDist())
    """
    all_text = " ".join(e for e in text_data)
    tokens = nltk.word_tokenize(all_text)
    """
    Alternatively, the following code results in the same effect except for punctuation marks.
    
        import re
        tokens = re.sub("[^\w]", " ",  all_text).split()
    """
    """
    Convert words to lowercase
    The following code becomes a moot, but I keep it for future ref.
    """
    #tokens_lower = [x.lower() for x in tokens]
    #tokens = tokens_lower
    
    """
    Remove stop words and punctuation marks
    """
    punc=[',','.','"',"'",'?','!',':',';',"$","<",">","(",")","-","—",'“','”']
    more_common_words = ["'d","'ll","'m","'re","'s","'ve","a.i","...","n't","would","us"]
    remove_words = set(stopwords.words('english')+punc+more_common_words)
    
    tokens_net = [i for i in nltk.word_tokenize(all_text.lower()) if i not in remove_words]
   
    print("total number of tokens: {}".format(len(tokens)))
    print("total number of unique words or punctuations: {}".format(len(set(tokens))))
    lexical_diversity = len(set(tokens))/len(tokens)
    print("lexical diversity: {}".format(lexical_diversity))
    
    """
    Calculate frequencies
    ref: http://www.nltk.org/book/ch01.html
    A halfway down the page, a table of functions of Freq distributions
    """
    
    freqD = nltk.FreqDist(tokens_net)
        
    """ 
    Write the word tokens (tokens_net) to a csv file 
    """
    fname = "FB_CEO_" + str(hearing_day) +".txt"
    with open (fname,'w') as FBfile:
        FBfile.write(' '.join(str(i) for i in tokens_net))
        
    return tokens_net, freqD