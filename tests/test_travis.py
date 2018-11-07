""" Containing unit tests"""
import os
import sys
# dir_path = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, dir_path.replace('/tests/core', '/'))
# print(sys.path)

import unittest
#from pandas.testing import assert_frame_equal
#import tempfile


class test_travis(unittest.TestCase):
    """Unit test for the MLDataFrame Class"""

    def setUp(self):
       self.test_var = "This is a travis test for CI" 

    def test_init(self):

        self.assertTrue(self.test_var == "This is a travis test for CI" )