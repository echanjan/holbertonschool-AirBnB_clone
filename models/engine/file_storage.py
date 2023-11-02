#!/usr/bin/python3
import json
from os import path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        if not path.exists(FileStorage.__file_path):
            return
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
