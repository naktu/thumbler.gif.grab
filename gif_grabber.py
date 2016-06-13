#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from lxml import html

FILEFORMAT = ".gif"


rss_xml = urllib.request.urlopen('http://ettoh.tumblr.com/rss').read()
root = ET.fromstring(rss_xml)
for child in root[0]:
    if child.tag == 'item':
        tree = html.fromstring(child.find('description').text)
        images = tree.xpath("//img/@src")
        for i in images:
            if i[-4:] == FILEFORMAT:
                print(i)