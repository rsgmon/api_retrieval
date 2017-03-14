import os
import requests
import json

"""Class
    init or call accepts a config object
    method: build get url builds url from config attributes we assume it has exactly what we want
    method: build post builds a post from the config parameters. Assume config has exactly what we want.
    method: using requests library make request and return data."""


class HTTPRequestHandler(object):
    def __init__(self, api_config_object=None):
        if api_config_object:
            self.config = api_config_object

    def post_request(self, api_config_object):
        return requests.post(api_config_object.route, json=api_config_object.parameters)
