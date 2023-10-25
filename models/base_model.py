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
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

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
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Este método regresa un diccionado.

        Returns:
            dict: Regresa un diccionario con los atributos de instancia.

        """
        attributes = self.__dict__.copy()
        attributes['__class__'] = self.__class__.__name__
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        return attributes
