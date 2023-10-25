#!/usr/rin/python3
"""
Este módulo define la clase BaseModel
"""

import uuid
import datetime


class BaseModel:

    """
    Esta clase define BaseModel
    """

    def __init__(self):
        """
        Este medoto inicializa lo sgte:
            id, created_at, update_at
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """
        Este método regresa a una representacion de nuestra instancia.

        Return:
            str: Representacion de instancia.
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Este método actualiza la fecha de creación updated_at.
        """
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        Este método regresa un diccionado.

        Returns:
            dict: Regresa un diccionario con los atributos de instancia.

        """
        self.__dict__['__class__'] = 'BaseModel'
        return self.__dict__
