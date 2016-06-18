#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from lxml import html
import time

# Configuration
FILEFORMAT = ".gif"     # checked file format
RSSFILE = "rss.txt"      # file with rss urls"
TIMEOUT = 10            # timeout second before check new url

# TODO Get gif liks - function return object GIF
# TODO Gif object:
#   Have attr: link, path
#   Have methods: get, hash
#   get get file in needed path
#   hash download file if path empty and create md5 hash
#   if path defined - create md5 hash
# TODO! Add tests for function and objects
# TODO Add loging and try statements

class Gif:
    gif_url = ""
    gif_path = ""
    md5_hash = 0

    def get_gif(self):
        pass

    def calculate_hash(self):
        pass
        

def get_rss_xml(rss_url):
    # Get xml from url

    # TODO Add try catch return errors
    rss_xml = urllib.request.urlopen(rss_url).read()
    return ET.fromstring(rss_xml)


def get_gifs(rss):
    # Get gifs link from xml

    links = []
    for child in rss[0]:
        if child.tag == 'item':
            description = child.find('description')
            if description is not None:
                tree = html.fromstring(description.text)
                images = tree.xpath("//img/@src")
                for i in images:
                    if i[-4:] == FILEFORMAT:
                        links.append(i)
    print(links)

if __name__ == "__main__":
    try:
        with open(RSSFILE) as rss_file:
            for url in rss_file:
                try:
                    rss = get_rss_xml(url)
                    get_gifs(rss)
                    print("sleep one second")
                    time.sleep(1)
                except:
                    print("Error: work url %s" % url)

            # TODO create function with check return of get_gifs answer

    except:
        print("ERROR cannot open the file %s" % RSSFILE)
        exit(1)
