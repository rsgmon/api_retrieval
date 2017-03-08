import argparse
import json
from .config import APIConfig
import sys

def parse_args(args):
    parser = argparse.ArgumentParser(description='Get some data from an API')
    parser.add_argument('path', help='get api request data from the file')
    return parser.parse_args(args)

def read_config_object(parsed_args):
    with open(parsed_args.path, 'r') as config_file:
        config_from_file = json.loads(config_file.read())
    config_object = APIConfig(config_from_file)
    return config_object
