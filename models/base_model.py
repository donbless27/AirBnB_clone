#!/usr/bin/python3
"""Defines the base model"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This is the class in AirBnB project where all other classes inherit from"""

    def _init_(self, *args, **kwargs):
        """Initializes the instance of a new BaseModel

        Args:
        *args: list of arguments
        **kwargs:keywords argument dict
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self._dict_["created_at"] = datetime.strptime(kwargs
                            ["created_at"], "%y-%m-%dT%H:%M:%s.%f")
                elif key == "updated_at":
                    self._dict_["updated_at"] = datetime.strptime(kwargs
                            ["updated_at"], "%y-%m-%dT%H:%M:%s.%f")
                else:
                    self._dict_[key] = kwargs[key]
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    storage.new(self)

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This returns a dictionary containing all keys/values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
                    
                    

