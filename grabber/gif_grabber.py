#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from lxml import html
import time
import random
import logging

# Configuration
import settings

# TODO Add loging and try statements
# TODO Last post date/time to file
logging.basicConfig(level=logging.INFO)

class Gif:
    def __init__(self):
        self.gif_url = ""
        self.gif_path = ""
        self.md5_hash = 0

    def get_gif(self, file_path):
        file_name = naming(16, len(settings.SYMBOLS),settings.SYMBOLS)
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

def naming(file_name_len, end, symbols):
    #Return randomize name for file
    file_name = ""
    for i in range(0, file_name_len, 1):
        file_name += symbols[random.randrange(0, end, 1)]
    return file_name

def get_gifs(rss, file_format):
    # Get gifs link from xml
    gifs = []
    for child in rss[0]:
        if child.tag == 'item':
            description = child.find('description')
            if description is not None:
                tree = html.fromstring(description.text)
                images = tree.xpath("//img/@src")
                for i in images:
                    if i[-4:] == file_format:
                        l = Gif()
                        l.gif_url = i
                        gifs.append(l)
                        logging.info("Finding gif %s" % l.gif_url)
                        #print(i)
    return gifs

def main(home_dir, rss_file, file_format):
    try:
        with open(home_dir + rss_file) as rss_file:
            for url in rss_file:
                rss = get_rss_xml(url)
                logging.info("Start rss url: %s" % url)
                if type(rss) is not dict:
                    gifs = get_gifs(rss, file_format)
                    if gifs != []:
                        for gif in gifs:
                            gif.get_gif(settings.FILE_PATH)
                            time.sleep(15)

                    else:
                        print("no gifs link")

                print("sleep one second")
                time.sleep(10)
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
        print("ERROR cannot open the file %s" % home_dir + rss_file)
        exit(1)
    except:
        # TODO add loging error
        print("Other error")
        exit(1)


if __name__ == "__main__":
    main(settings.HOME_DIR, settings.RSS_FILE, settings.FILE_FORMAT)