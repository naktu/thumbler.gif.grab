#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from lxml import html
import time
import random

# Configuration
import settings

# TODO Add loging and try statements
# TODO Last post date/time to file


class Gif:
    def __init__(self):
        self.gif_url = ""
        self.gif_path = ""
        self.md5_hash = 0

    def get_gif(self, file_path):
        file_name = naming()
        urllib.request.urlretrieve(self.gif_url, file_path + file_name)

    def calculate_hash(self):
        #TODO if md5_hash is empty to create hash for this file
        pass

    def move_file(self, filename, destination):
        pass

def get_rss_xml(rss_url):
    # Get xml from url
    # TODO Add try catch return errors
    try:
        rss_xml = urllib.request.urlopen(rss_url).read()
    except:
        # TODO logging error type
        return({"ERROR": "url error"})

    try:
        xml  = ET.fromstring(rss_xml)
    except:
        # TODO logging error type
        return({"ERROR": "xml error"})

    return xml

def naming(file_name_len, end):
    #Return randomize name for file
    file_name = ""
    for i in range(0, file_name_len, 1):
        file_name += settings.SYMBOLS[random.randrange(0, end, 1)]
    return file_name

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
                    if i[-4:] == settings.FILE_FORMAT:
                        l = Gif()
                        l.gif_url = i
                        gifs.append(l)
                        #print(i)
    return gifs

def main():
    try:
        with open(settings.HOME_DIR + settings.RSS_FILE) as rss_file:
            for url in rss_file:
                rss = get_rss_xml(url)
                if type(rss) is not dict:
                    gifs = get_gifs(rss)
                    if gifs != []:
                        for gif in gifs:
                            print(gif.gif_url)
                    else:
                        print("no gifs link")

                print("sleep one second")
                time.sleep(1)
            # TODO maybe willn't use whit and change to open file becase if error no open file
            # it return file error
            # TODO сделать так как в примере книги, про вызов ошибок, это позволит
            #      переопределить тип ошибки самостоятельно и далее удобно будет
            #      тестировать
            # TODO попробовать сделать тестирование ошибок все же более грамотно,
            #      см. описание на странице 24-25 книги про тестирование
            # TODO create function with check return of get_gifs answer

    except FileNotFoundError:
        # TODO add loging error
        print("ERROR cannot open the file %s" % settings.HOME_DIR + settings.RSS_FILE)
        exit(1)
    except:
        # TODO add loging error
        print("Other error")
        exit(1)


if __name__ == "__main__":
    main()