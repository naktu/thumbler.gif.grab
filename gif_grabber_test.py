#!/usr/bin/env python3

import unittest
from gif_grabber import *
import xml.etree.ElementTree as ET
import urllib.request

class TestGetRssXml(unittest.TestCase):
    def setUp(self):
        self.valid_url    = "http://animesquads.tumblr.com/rss"
        self.no_exist_url = "http://animesquads.sdfsdfsdf12=.com/rss"
        self.no_rss_url   = "http://animesquads.tumblr.com"

    def test_valid_rss_url(self):
        self.assertEqual(ET.Element, type(get_rss_xml(self.valid_url)))
    
    def test_url_unvaliable(self):
        pass

    def test_no_rss_url(self):
        self.assertRaises(ET.ParseError, get_rss_xml(self.no_rss_url))

if __name__ == "__main__":
    unittest.main()