#!/usr/bin/python3
"""
Este módulo expone la clase
HBNBCommand(cmd.Cmd)
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Esta clase hereda de cmd.Cmd, desde aqui se gestionará
    nuestro proyecto.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
