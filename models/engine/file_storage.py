#!/usr/bin/python3
"""This module contains the Filetorage class"""

import json
"""The json module for serializaion and deserialization"""

class FileStorage():
    """The FileStorage class that serializes instances to
        a JSON file and deserializes JSON file to instances
        Args:
            __file_path: Private class attribute
             string - path to the JSON file
             __objects: private class attribute
             dictionary - empty but will store all objects 
        """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = f"{self.__class__.__name__}.{self.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """

        with open(self.__file_path, "w") as file:
            new = {k : v.to_dict()  for k, v in self.__objects.items()}
