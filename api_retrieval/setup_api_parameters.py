import argparse
import json
import os
import sys

def parse_args(args):
    parser = argparse.ArgumentParser(description='Get some data from an API')
    parser.add_argument('file', help='get api request data from the file')
    return parser.parse_args(args)

def load_configuration_file():
    current_working_directory = os.path.dirname(os.path.realpath(__file__))
    parser = parse_args(sys.argv[1:])

    with open(os.path.join(current_working_directory, parser.file), 'r') as t:
        myjson = t.readline()


