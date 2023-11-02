#!/usr/bin/python3
import unittest

from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    def test_file_path(self):
        self.assertIsNone(FileStorage.__file_path)
