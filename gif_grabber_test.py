#!/usr/bin/env python3
import unittest
import gif_grabber

class TestGetRssXml(unittest.TestCase):
    def setUP(self):
        valid_url    = "http://animesquads.tumblr.com/rss"
        no_exist_url = "http://animesquads.dtumblr.com/rss"

    def test_valid_rss_url(self):
        #TODO check valid url
        pass
    
    def test_url_unvaliable(self):
        #TODO check with no_exist_url
        pass

    def test_no_rss_url(self):
        #TODO check if url no rss
        pass