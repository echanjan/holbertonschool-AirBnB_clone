#!/usr/bin/python3
"""Define la clase State"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Define el nombre del estado de la ciudad

    Atributos:
        name(str): Estado de la ciudad
    """

    name = ""
