class APIConfig(object):
    def __init__(self, config_file):
        self.path = config_file['base_url']
        self.entity = config_file['entity']
