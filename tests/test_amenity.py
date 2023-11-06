#!/usr/bin/python3
import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_compare_attrs(self):
        amenity_attr = self.amenity.to_dict()
        self.assertNotIn("name", amenity_attr)
