#!/usr/bin/python3
"""filestrorage module"""
import json
from models.base_model import BaseModel
import os

class FileStorage:
    """filestorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        tmp = {}
        with open(self.__file_path, mode='w+', encoding="utf-8") as wjsonf:
            for i, j in self.__objects.items():
                tmp[i] = j.to_dict()
            json.dump(tmp, wjsonf)

    def reload(self):
        """deserializes the JSON file to __objects"""

        current_classes = {'BaseModel': BaseModel}

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
