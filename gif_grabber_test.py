#!/usr/bin/env python3

import unittest
from gif_grabber import *
import xml.etree.ElementTree as ET
import urllib.request

class TestGetRssXml(unittest.TestCase):
    def setUp(self):
        self.valid_url    = "http://animesquads.tumblr.com/rss"

    def test_valid_rss_url(self):
        self.assertEqual(ET.Element, type(get_rss_xml(self.valid_url)))


if __name__ == "__main__":
    unittest.main()