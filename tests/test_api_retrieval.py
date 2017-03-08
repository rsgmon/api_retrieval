#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_api_retrieval
----------------------------------

Tests for `api_retrieval` module.
"""


import sys
import unittest
from api_retrieval.parse_args  import parse_args



class TestApi_retrieval(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_args_correct(self):
        parser = parse_args(['filename'])
        self.assertTrue(parser.file)
