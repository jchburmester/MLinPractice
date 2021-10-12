# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:39:42 2021

@author: Beck
"""
import ast
from code.feature_extraction.feature_extractor import FeatureExtractor

class BigramFeature(FeatureExtractor):
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_bigrams".format(input_column))
        
    def _set_variables(self, inputs):
        
        overall_text = []
        for line in inputs:
            tokens = ast.literal_eval(line.item())
            overall_text += tokens

        self._bigrams = []
        