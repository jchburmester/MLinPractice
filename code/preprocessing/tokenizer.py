# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:52:12 2021

@author: Beck
"""

"""
Tokenize the tweet into individual words
"""
from code.preprocessing.preprocessor import Preprocessor
import nltk

class Tokenizer(Preprocessor):
    """ Tokenizes the input column into individual words """
    
    def _init_(self, input_column, output_column):
        """Initialize the Tokenizer with the given in and output column"""
        super()._init_([input_column], output_column)
        
    def _get_values(self, inputs):
        "Tokenize the tweet"
        
        tokenized = []
        
        for tweet in inputs[0]:
            sentences = nltk.sent_tokenize(tweet)
            tokenized_tweet = []
            for sentence in sentences:
                words = nltk.word_tokenize(sentence)
                tokenized_tweet += words
                
            tokenized.append(str(tokenized_tweet))
            
        return tokenized