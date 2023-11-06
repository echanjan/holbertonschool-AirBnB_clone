#!/usr/bin/python3
import unittest

from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_compare_attrs(self):
        state_dict = self.state.to_dict()
        self.assertNotIn("name", state_dict)
