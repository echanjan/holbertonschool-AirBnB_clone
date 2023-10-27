#!/usr/rin/python3
"""
Importamos los módulos 'uuid' y 'datetime' para generar identificadores únicos
y para trabajar con fechas y horas.
"""

import uuid
import datetime

"""
Definimos una clase llamada BaseModel
"""


class BaseModel:

    """
    Metodo de inicialización que se ejecuta cuando se crea una
    nueva instancia de la clase.
    """

    def __init__(self, *args, **kwargs):
        """
        Asignamos un identificador único generado por 'uuid.uuid4()'
        y lo convertimos a una cadena.

        Asignamos la fecha y hora actuales al momento de creación
        de la instancia.

        Asignamos la fecha y hora actuales al atributo 'updated_at' también
        para que esté igual al momento de creación al principio.
        """

        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            self.__dict__["created_at"] = datetime.strptime(
                self.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

            self.__dict__["updated_at"] = datetime.strptime(
                self.__dict__["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    """
    Método especial que define cómo se imprimirá una instancia de la clase
    cuando se use la función 'print()'.
    """
    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    """
    Método 'save' que actualiza el atributo 'updated_at'
    con la fecha y hora actuales.
    """
    def save(self):
        self.updated_at = datetime.datetime.now()

    """
    Método 'to_dict' que retorna un diccionario con los atributos
    de la instancia.
    """
    def to_dict(self):
        """
        Copiamos el diccionario de atributos usando 'self.__dict__.copy()'

        Añadimos una clave '__class__' al diccionario que contiene
        el nombre de la clase.

        Convertimos las fechas y horas a una cadena en formato ISO.

        Retornamos el diccionario modificado.
        """
        attributes = self.__dict__.copy()
        attributes['__class__'] = self.__class__.__name__
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        return attributes
