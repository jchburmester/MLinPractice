# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:50:46 2021

@author: Beck
"""

import unittest
import pandas as pd
from code.preprocessing.tokenizer import Tokenizer
class TokenizerTest(unittest.TestCase):
    
    def test_boolean(self):
        self.assertEqual(True, not False)
        
if __name__ == '__main__':
    unittest.main()