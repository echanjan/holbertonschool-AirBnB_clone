#!/usr/bin/python3
import unittest

from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_compare_attrs(self):
        review_attr = self.review.to_dict()
        self.assertNotIn("place_id", review_attr)
        self.assertNotIn("user_id", review_attr)
        self.assertNotIn("text", review_attr)
