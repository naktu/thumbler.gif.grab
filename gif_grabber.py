#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from lxml import html
import time

# Configuration
FILEFORMAT = ".gif"     # checked file format
RSSFILE = "rss.txt"      # file with rss urls"
TIMEOUT = 10            # timeout second before check new url

# TODO Add loging and try statements

class Gif:
    gif_url = ""
    gif_path = ""
    md5_hash = 0

    def get_gif(self, file_path):
        #TODO get file to file_path
        pass

    def calculate_hash(self):
        #TODO if md5_hash is empty to create hash for this file
        pass


def get_rss_xml(rss_url):
    # Get xml from url

    # TODO Add try catch return errors
    rss_xml = urllib.request.urlopen(rss_url).read()
    return ET.fromstring(rss_xml)


def get_gifs(rss):
    # Get gifs link from xml

    gifs = []
    for child in rss[0]:
        if child.tag == 'item':
            description = child.find('description')
            if description is not None:
                tree = html.fromstring(description.text)
                images = tree.xpath("//img/@src")
                for i in images:
                    if i[-4:] == FILEFORMAT:
                        l = Gif
                        l.gif_url = i
                        gifs.append(l)
    return gifs

if __name__ == "__main__":
    try:
        with open(RSSFILE) as rss_file:
            for url in rss_file:
                try:
                    rss = get_rss_xml(url)
                    gifs = get_gifs(rss)
                    print("sleep one second")
                    time.sleep(1)
                except:
                    print("Error: work url %s" % url)

            # TODO create function with check return of get_gifs answer

    except:
        print("ERROR cannot open the file %s" % RSSFILE)
        exit(1)
