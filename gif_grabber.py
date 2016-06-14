#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from lxml import html

FILEFORMAT = ".gif"

#TODO Get gif liks - function return object GIF
#TODO Gif object:
    # Have attr: link, path, 
    # Have methods: get, hash
    # get get file in needed path
    # hash download file if path empty and create md5 hash
    # if path defined - create md5 hash
#TODO! Add tests for function and objects       

def get_gifs():
    links = []
    rss_xml = urllib.request.urlopen('http://ettoh.tumblr.com/rss').read()
    root = ET.fromstring(rss_xml)
    for child in root[0]:
        if child.tag == 'item':
            tree = html.fromstring(child.find('description').text)
            images = tree.xpath("//img/@src")
            for i in images:
                if i[-4:] == FILEFORMAT:
                    links.append(i)
    print(links)

if __name__ == "__main__":
    get_gifs()