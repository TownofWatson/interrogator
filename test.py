import unittest
import watson
import sys
import os
import json
import time
import webbrowser
import mimetypes
#import easygui
import nltk
from textblob import TextBlob
from textblob import Word
from watson_developer_cloud import DiscoveryV1
import random
import ctypes  



class DefaultProcessWho(unittest.TestCase):
    def test_process_who_query(self):
        result_process = watson.process_who_query("xyz")
        self.assertTrue(result_process)




class DefaultPrintTest(unittest.TestCase):
    def test_print_to_html(self):
    	result_print = watson.print_to_html("pdfs/gen/report_test_1.pdf")
    	self.assertTrue(result_print)


test_process = DefaultProcessWho('test_process_who_query')
test_print = DefaultPrintTest('test_print_to_html')

test_process.test_process_who_query()
test_print.test_print_to_html()