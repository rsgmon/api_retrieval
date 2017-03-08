class APIConfig(object):
    def __init__(self, config_file):
        self.path = config_file[0]['base_url']
        self.entity = config_file[1]['entity']
