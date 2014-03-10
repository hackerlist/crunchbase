#-*- coding: utf-8 -*-

"""
    crunchbase.test
    ~~~~~~~~~~~~~~~

    Test cases for the crunchbase api
"""

import unittest
import os
from crunchbase import Crunchbase

TEST_API_KEY = 'dr66y8dsr72hct67pmd6xqqf'

class TestCrunchbase(unittest.TestCase):
    
    def test_connection(self):
        cb = Crunchbase(TEST_API_KEY)

    def test_get_company(self):
        cb = Crunchbase(TEST_API_KEY)
        x = cb.company('crunchbase')

