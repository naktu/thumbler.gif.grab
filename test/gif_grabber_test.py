#!/usr/bin/env python3

import os
import unittest
import xml.etree.ElementTree as ET
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grabber import gif_grabber

class TestGetRssXml(unittest.TestCase):
    def setUp(self):
        self.valid_url = "http://animesquads.tumblr.com/rss"
        self.no_rss_url = "https://google.com/"
        self.no_valid_url = "https://123.len.file.name11"

    def test_valid_rss_url(self):
        self.assertEqual(ET.Element, type(gif_grabber.get_rss_xml(self.valid_url)))

    def test_no_rss(self):
        self.assertEqual("url error", gif_grabber.get_rss_xml(self.no_valid_url)["ERROR"])

    def test_no_valid_url(self):
        self.assertEqual("xml error", gif_grabber.get_rss_xml(self.no_rss_url)["ERROR"])

class TestNaming(unittest.TestCase):
    def setUp(self):
        self.end = len(gif_grabber.SYMBOLS)
        self.file_name_len = 16  

    def test_name_len(self) :
        self.assertEqual(self.file_name_len, len(gif_grabber.naming(self.file_name_len, self.end)))

    def test_name_type(self):
        self.assertEqual(str, type(gif_grabber.naming(self.file_name_len, self.end)))

if __name__ == "__main__":
    unittest.main()
