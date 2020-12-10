import pandas as pd
import os
import xmltodict as xmltd
import requests
from datetime import datetime
from Connectors import RobotTXTReader as rtxt

xmlDict = {}


def generate_raw(url):
    result = requests.get(url)
    results_str = result.text
    # result_parsed = ET.parse(results_str["sitemapindex"]["sitemap"])
    result_raw = xmltd.parse(results_str)
    return result_raw


def get_sitemaps(url):
    sitemap_raw = generate_raw(url)
    sitemap_keys = sitemap_raw["sitemapindex"]["sitemap"]
    current_timestamp = datetime.now()  # To keep track of the crawl refreshes
    sitemap_list = [[raw["loc"], current_timestamp] for raw in sitemap_raw["sitemapindex"]["sitemap"]]
    sitemap_df = pd.DataFrame(sitemap_list, columns=["links", "lastcrawled"])
    return sitemap_df

def get_posts_url(url):
    sitemap_df = get_sitemaps(url)
    post_url = sitemap_df[sitemap_df["links"].str.contains("post", na=False)]
    return post_url["links"]

def get_posts(url):
    # post_url = get_posts_url(url)
    result = requests.get("https://lycia.org/post-sitemap.xml")
    results_str = result.text
    result_raw = xmltd.parse(results_str)
    current_timestamp = datetime.now()  # To keep track of the crawl refreshes
    sitemap_list = [[raw["loc"],
                     raw["lastmod"],
                     raw["changefreq"],
                     current_timestamp] for raw in result_raw["urlset"]["url"]]
    sitemap_df = pd.DataFrame(sitemap_list, columns=["links", "lastmod", "changefreq", "lastcrawled"])
    return sitemap_df
