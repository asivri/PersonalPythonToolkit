# Tutorial Source: https://www.jcchouinard.com/robots-txt-parsing-with-python/

import pandas as pd
import os
from urllib.parse import urlparse


# base_url = https://lycia.org/sitemap.xml
# TODO: Create way to
def generate_url(url):
    base_url = '{uri.scheme}://{uri.netloc}'.format(
        uri=urlparse(url))  # TODO: Take a look at ways to improve&understand this.
    robot_url = base_url + '/robots.txt'
    return robot_url


def read_robots_file(url):
    robot_url = generate_url(url)
    robot_file = os.popen(f'curl {robot_url}').read()
    return robot_file


# Create a dictionary to insert data.
# TODO: Move function to Data.py
def find_sitemap(robot_file):
    result_ds = {'Sitemap': {}}  # Result dataset to return
    for line in robot_file.split("\n"):
        if line.startswith("Sitemap:"):
            result_ds['Sitemap'].update({line.split('Sitemap:')[1].strip():{}}) #Retrieves substring after "Sitemap:"
            #Generates a substring.
            keys = []
    for key in result_ds['Sitemap'].keys():
        keys.append(key)
    return result_ds, keys


# Parse the sitemap into a dictionary
def generate_dictionary(url):
    robots = read_robots_file(url)
    sitemap = find_sitemap(robots)
    # Example output:
    # ({'Sitemap': {'Sitemap: https://lycia.org/sitemap.xml': {}}}, ['Sitemap: https://lycia.org/sitemap.xml'])
    result_ds = sitemap[0].get('Sitemap')
    keys = sitemap[1]
    # for i in range(len(
    #         keys)):  # TODO: Now it doesn't make sense to loop for single item but i'm planning to add base url + sitemap to store multiple sites.
    #     if i <= len(keys) - 2:
    #         end_str = keys[i + 1]
    #         print(end_str)
    #     else:
    #         end_str = 'End of function'
    #     # result_ds['Sitemap'][keys[i]]['Sitemap'] = []
    return result_ds

