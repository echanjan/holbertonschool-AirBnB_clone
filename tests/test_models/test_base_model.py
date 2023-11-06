#!/usr/bin/python3

import unittest

from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.bm = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.bm.id, str)

    def test_return(self):
        self.assertIsNone(self.bm.save())

    def test_compare_attrs(self):
        model_dict = self.bm.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)

    def test_methods_magic_str(self):
        bm = BaseModel()
        expected_output = f"[{bm.__class__.__name__}] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected_output)

    def test_update_date(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        original_created_at = model.created_at
        time.sleep(1)
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)
        self.assertTrue(original_created_at, model.created_at)
        self.assertNotEqual(model.updated_at, model.created_at)

    def test_save(self):
        model = BaseModel()
        self.assertIsNone(model.save())

    def test_update_type(self):
        model = BaseModel()
        self.assertTrue(type(model.updated_at) == datetime)


if __name__ == "__main__":
    unittest.main()
