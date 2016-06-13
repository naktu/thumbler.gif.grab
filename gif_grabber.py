#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from lxml import html


rss_xml = urllib.request.urlopen('http://ettoh.tumblr.com/rss').read()
root = ET.fromstring(rss_xml)
g = 0
for child in root[0]:
    g = g+1
    if child.tag == 'item':
        tree = html.fromstring(child.find('description').text)
        images = tree.xpath("//img/@src")
        for i in images:
            print(i[-3:])