from api_retrieval.config import APIConfig

test_config = [{"base_url": "http://www.urlbase.com", "entity": "0984752039578e4r"}, {"base_url": "http://www.urlbase.com", "entity": "0984752039578e4r"}]
api_config = [APIConfig(x) for x in test_config]
