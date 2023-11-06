#!/usr/bin/python3
"""En este modulo creamos la clase user"""

from models.base_model import BaseModel


class User(BaseModel):
    """Esta clase maneja los atributos del user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
