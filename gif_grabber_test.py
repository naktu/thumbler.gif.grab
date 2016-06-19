#!/usr/bin/env python3

import unittest
from gif_grabber import *
import xml.etree.ElementTree as ET
import urllib.request
import string
import random

class TestGetRssXml(unittest.TestCase):
    def setUp(self):
        self.valid_url = "http://animesquads.tumblr.com/rss"

    def test_valid_rss_url(self):
        self.assertEqual(ET.Element, type(get_rss_xml(self.valid_url)))

class TestNaming(unittest.TestCase):
    def setUp(self):
        self.SYMBOLS = string.ascii_uppercase + string.digits + string.ascii_uppercase.lower()
        self.end= len(self.SYMBOLS)
        self.file_name_len = 16  

    def test_name_len(self) :
        self.assertEqual(self.end, len(naming(self.file_name_len, self.end)))

    def test_name_type(self):
        self.assertEqual(string, type(naming(self.file_name_len, self.end)))

if __name__ == "__main__":
    unittest.main()
