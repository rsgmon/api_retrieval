#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_api_retrieval
----------------------------------

Tests for `api_retrieval` module.
"""


import sys
import unittest
from api_retrieval.setup_api_parameters import *
from tests.test_data.test_data import test_config



class TestApi_retrieval(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_args_correct(self):
        parser = parse_args(['filename'])
        self.assertTrue(parser.path)

    def test_001_path_correct(self):
        parser = parse_args(['C:\\Users\\Rye\\Google Drive\\School\\Python\\cli_apps\\api_retrieval\\tests\\test_data\\test_config.json'])
        read_config_object(parser)
        self.assertEqual(test_config[0]['base_url'], read_config_object(parser).path)
