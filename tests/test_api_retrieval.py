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
from tests.test_data.test_data import test_config, api_config


class TestApi_retrieval(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_args_correct(self):
        parser = parse_args(['filename'])
        self.assertTrue(parser.path)

    def test_001_path_correct(self):
        config_collection = read_config_file(None)
        self.assertEqual(config_collection, None)

    def test_002_create_config_collection(self):
        config_collection = test_config
        apiconfig_collection = create_config_collection(config_collection)
        self.assertEqual(apiconfig_collection[0].entity, api_config[0].entity)
