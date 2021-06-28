import configparser
import os


def read_properties():
    config = configparser.ConfigParser()
    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = root_path + os.sep + '..' + os.sep + 'config' + os.sep + 'environment.properties'
    config.read(file_path)
    return config