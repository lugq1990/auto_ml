# -*- coding:utf-8 -*-
"""
Whole relative functions used for files

@author: Guangqiang.lu
"""
import yaml


def load_yaml_file(file_path):
    """
    load yaml files from local return is JSON dict
    :param file_path:
    :return: dictionary
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.load(file)
    except IOError as e:
        raise IOError("When load file: {} with error: {}".format(file_path, e))
