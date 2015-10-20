import copy
import os

__author__ = 'SilviyaSoti'

import json
from pprint import pprint
import unittest
from IPythonProject import githubparsing


# Unit Tests
class TestJSONMethods(unittest.TestCase):

    # read from json file
    temp_path = os.path.dirname(os.path.realpath("UnitTests"))
    print "Temp Path: ", temp_path
    with open(temp_path.replace("UnitTests", "") + '/IPythonProject/data_copy.json') as data_file:
        data = json.load(data_file)

    def test_totalcount(self):
        total_count = self.data["total_count"]
        self.assertEqual(total_count, 1109)

    def test_numberitems(self):
        items = self.data["items"]
        number_items = len(items)
        self.assertEqual(number_items, 30)

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()