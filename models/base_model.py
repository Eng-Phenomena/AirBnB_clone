#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """base model class"""

    def __init__(self, *args, **kwargs):
        """Constructor of BaseModel
        ....................................
            args:
            ...
            self -> instance
            args -> variable number of variable in tuple
            kwargs -> key word argument to get dict
        """

        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """To string method of instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updating the time of object"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        Updated_Dict = self.__dict__.copy()
        Updated_Dict["__class__"] = self.__class__.__name__
        Updated_Dict["updated_at"] = self.updated_at.isoformat()
        Updated_Dict["created_at"] = self.created_at.isoformat()

        return Updated_Dict
