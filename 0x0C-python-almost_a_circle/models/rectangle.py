#!/usr/bin/python3
""" New class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from class Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
