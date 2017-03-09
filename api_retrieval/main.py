# -*- coding: utf-8 -*-
import api_retrieval.setup_api_parameters
import sys

if __name__ == "__main__":
    config = api_retrieval.setup_api_parameters.config_operation()


# So we have a config file, now normally we would then pass this to url generator, but we want the url generator to accept a config o
