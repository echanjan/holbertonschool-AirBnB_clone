#!/usr/bin/python3
import unittest

from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_compare_attrs(self):
        city_attr = self.city.to_dict()
        self.assertNotIn("state_id", city_attr)
        self.assertNotIn("name", city_attr)
