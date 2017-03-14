#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_api_retrieval
----------------------------------

Tests for `api_retrieval` module.
"""


import sys
import unittest
import requests
from api_retrieval.setup_api_parameters import *
from tests.test_data.test_data import test_config, api_config, single_api_config, api_config_with_key_route
from api_retrieval.http_request import HTTPRequestHandler
import api_retrieval.config


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
        self.assertTrue(isinstance(apiconfig_collection[0], api_retrieval.config.APIConfig))

    def test_003_setup_http_request_object(self):
        http_request_handler = HTTPRequestHandler(single_api_config)
        self.assertTrue(type(http_request_handler.config) == APIConfig)

    def test_004_construct_configuration(self):
        test_route = "http://www.testing.com/my_route"
        test_parameter = {'api_key': '20349587', 'entity': '0984752039578e4r'}
        self.assertEqual(single_api_config.route, test_route)
        self.assertEqual(single_api_config.parameters, test_parameter)

    def test_005_construct_configuration_with_api_key_route(self):
        test_route = "http://www.testing.com/my_route/20349587"
        self.assertEqual(api_config_with_key_route.route, test_route)

