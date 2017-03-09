# -*- coding: utf-8 -*-
import api_retrieval.setup_api_parameters
import sys

if __name__ == "__main__":
    config = api_retrieval.setup_api_parameters.config_operation()
    [print(x) for x in config]

# So we have a collection of configuation objects, each of these objects is passed to a url generator. This in turn will return json for processing

"""
Class
    init or call accepts a config object
    method build url takes the config parameters and does the building. we assume it has everything"""
