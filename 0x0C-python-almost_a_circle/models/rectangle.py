#!/bin/usr/python3

from models.base import Base

class Rectangle(Base):
    """rectangle class inherits from base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is a class constructor for the rectangle"""

        super().__init__(id)
        #private instances with getters and setters

        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__Y = 0

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value if value > 0 else 0

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value if value > 0 else 0
        
        @property
        def x(self):
            return self.__x
        @x.setter
        def x(self, value):
            self.__x = value if value >= 0 else 0

        @property
        def y(self):
            return self.__y
        @y.setter
        def y(self, value):
            self.__y = value if value >= 0 else 0


