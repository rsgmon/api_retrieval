import argparse
import json
from .config import APIConfig
import sys

def parse_args(args=None):
    if not args: return None
    parser = argparse.ArgumentParser(description='Path to the config file.')
    parser.add_argument('path', help='Specify the absolute path of the config file.')
    return parser.parse_args(args)

def read_config_file(file_path):
    if not file_path: return None
    with open(file_path.path, 'r') as config_file:
        config_object = json.loads(config_file.read())
        if type(config_object) != type([]):
            config_object = [config_object]
    return config_object

def create_config_collection(config_collection):
    return [APIConfig(x) for x in config_collection]

def config_operation():
    parsed = parse_args(sys.argv[1:])
    return create_config_collection(read_config_file(parsed))

#So I read a json object from the json file which can contain many config objects.  I then return a collection of config objects. Now what I could do is say "hey I want to run this with a parameter one time and get data, or I want this to run everytime it checks a folder and that folder has changed, or if I input a variable I get a menu that allows me to run via inputing a config file location.
