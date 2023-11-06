#!/usr/bin/python3
"""
Este modulo define la clase de FileStorage
"""

import json
from os import path


class FileStorage:
    """
    La clase FileStorahe se encargará de serializar y
    deserealizar archivos para recuperar instancias de BaseModel
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retoma el contenido de .__objects.
        Returns:
            dict
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Este método almacena las instancias de clase,
        recibidas en .__objects.
        Args:
            obj (objecs): Instancias a almacenar.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Este método guarda un diccionario retornado de las
        instancias almacenadas en.__objects.
        Return:
            None
        """
        new_dict = {}

        for k, obj in FileStorage.__objects.items():
            for k, obj in FileStorage.__objects.items():
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Este método lee un archivo en formato .json, que se guardo
        previamente con el método .save(), el diccionario recuperado
        se convertirá a objetos de python (dict) que seran utilizados
        para recuprar las instancias de clase BaseModel creadas
        anteriormente, estas instancias serán almacenadas en .__objects.
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as json_file:
                objs = json.load(json_file)
            for k, v in objs.items():
                from models.base_model import BaseModel
                bs = BaseModel(**v)
                FileStorage.__objects[k] = bs
