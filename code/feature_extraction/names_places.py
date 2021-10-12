# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:05:45 2021

@author: Beck
"""

import nltk
from code.feature_extraction.feature_extractor import FeatureExtractor

class NamesPlacesFeature(FeatureExtractor):
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_names_places".format(input_column))
        
    def _set_variables(self, inputs):
        
        sentences = nltk.sent_tokenize(inputs)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            pos_tagged = nltk.pos_tag(words)
            ne_chunked = nltk.ne_chunk(pos_tagged)
            print(ne_chunked)
            