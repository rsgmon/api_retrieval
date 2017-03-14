# -*- coding: utf-8 -*-
import os
import api_retrieval.setup_api_parameters
import api_retrieval.http_request

if __name__ == "__main__":
    config_collection = api_retrieval.setup_api_parameters.config_operation()
    for config in config_collection:
        http_request = api_retrieval.http_request.HTTPRequestHandler(config)
        print(http_request.post_request(http_request.config).json())
