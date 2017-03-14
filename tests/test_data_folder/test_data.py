from api_retrieval.config import APIConfig

test_config = [{"base_path": "http://www.testing.com", "entity": "0984752039578e4r", "route": "my_route", "api_key": "20349587"}, {"base_path": "http://www.urlbase.com", "entity": "0984752039578e4r", "route": "my_route", "api_key": "20349587"}]
api_config = [APIConfig(x) for x in test_config]
single_api_config = APIConfig(test_config[0])
api_config_with_key_route = APIConfig({"base_path": "http://www.testing.com", "entity": "0984752039578e4r", "route": "my_route", "api_key_route": "20349587"})
