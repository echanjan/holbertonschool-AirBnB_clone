#!/usr/bin/python3
import unittest

from models.place import Place


class TestCity(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_compare_attrs(self):
        place_attr = self.place.to_dict()
        self.assertNotIn("city_id", place_attr)
        self.assertNotIn("user_id", place_attr)
        self.assertNotIn("name", place_attr)
        self.assertNotIn("description", place_attr)
        self.assertNotIn("number_rooms", place_attr)
        self.assertNotIn("number_bathrooms", place_attr)
        self.assertNotIn("max_guest", place_attr)
        self.assertNotIn("price_by_night", place_attr)
        self.assertNotIn("latitude", place_attr)
        self.assertNotIn("longitude", place_attr)
        self.assertNotIn("amenity_ids", place_attr)
