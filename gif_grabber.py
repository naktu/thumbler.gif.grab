#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from lxml import html
import time

FILEFORMAT = ".gif"
RSSFILE= "rss.txt"

#TODO Get gif liks - function return object GIF
#TODO Gif object:
    # Have attr: link, path, 
    # Have methods: get, hash
    # get get file in needed path
    # hash download file if path empty and create md5 hash
    # if path defined - create md5 hash
#TODO! Add tests for function and objects    
#TODO Add loging and try statements
#TODO function get_gifs only get gifs from xml, get xml from ulr another function.     

def get_rss_xml(rss_link):
    rss_xml = urllib.request.urlopen(rss_link).read()
    return ET.fromstring(rss_xml)   

def get_gifs(rss):
    links = []
    for child in rss[0]:
        if child.tag == 'item':
            description = child.find('description')
            if description != None:
                tree = html.fromstring(description.text)
                images = tree.xpath("//img/@src")
                for i in images:
                    if i[-4:] == FILEFORMAT:
                        links.append(i)
    print(links)

if __name__ == "__main__":
    with open(RSSFILE) as rss_file:
        for link in rss_file:
            rss = get_rss_xml(link)
            get_gifs(rss)
            print("sleep one second")
            time.sleep(1)