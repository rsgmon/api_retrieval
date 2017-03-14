import os

class APIConfig(object):
    def __init__(self, config_raw):
        self.config_from_file = config_raw
        self.construct_configuration(self.config_from_file)

    def _construct_route(self, config_raw):
        self.route = config_raw['base_path'] + "/" + config_raw['route']
        if 'api_key_route' in config_raw:
            if config_raw['api_key_route']:
                self.route = self.route + "/" + config_raw['api_key_route']

    def _objectify_parameters(self, config_raw):
        self.parameters = {}
        for parameter in config_raw:
            if parameter == 'base_path' or parameter == 'route' or parameter == 'api_key_route':
                continue
            self.parameters[parameter] = config_raw[parameter]

    def construct_configuration(self, config_raw):
        self._construct_route(config_raw)
        self._objectify_parameters(config_raw)
