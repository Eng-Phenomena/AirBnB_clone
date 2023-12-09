#!/usr/bin/python3
"""FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances

    <class 'BaseModel'> -> to_dict() -> <class 'dict'> ->
    JSON dump -> <class 'str'> -> FILE -> <class 'str'> ->
    JSON load -> <class 'dict'> -> <class 'BaseModel'>

"""

from models.base_model import BaseModel
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """File storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the stored dict"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
            args:

            self -> instance variable
            obj -> obj to be stored
        """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __filepath)"""

        tmp = {}
        with open(self.__file_path, mode='w', encoding="utf-8") as wjsonf:
            for i, j in self.__objects.items():
                tmp[i] = j.to_dict()
            json.dump(tmp, wjsonf)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(FileStorage.__file_path) as f:
                tmp_dict = json.load(f)
                for value in tmp_dict.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
