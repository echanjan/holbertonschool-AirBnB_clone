#!/usr/bin/python3
import unittest

from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.Us = User()

    def test_compare_attrs(self):
        user_dict = self.Us.to_dict()
        self.assertNotIn("email", user_dict)
        self.assertNotIn("password", user_dict)
        self.assertNotIn("first_name", user_dict)
        self.assertNotIn("last_name", user_dict)
