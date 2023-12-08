#!/usr/bin/python3
""" Base model"""
from datetime import datetime
import uuid
import models

class BaseModel:
    """ Base mOdel class"""
    def __init__(self, *args, **kwargs):
        """ constructor of base model"""

        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ to string method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ upadting time of the instance"""
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returnig key/value of the instance"""
        Updated_dict = self.__dict__.copy()

        Updated_dict["__class__"] = self.__class__.__name__
        Updated_dict["updated_at"] = self.updated_at.isoformat()
        Updated_dict["created_at"] = self.created_at.isoformat()

        return (Updated_dict)
