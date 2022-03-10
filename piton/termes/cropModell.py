from ctypes import sizeof
from sunau import Au_read
from unicodedata import name


class CropModell:
    def __init__(self,id,name,area,size,height,year):
        self.id = id
        self.name = name
        self.area = area
        self.size = size
        self.height = height
        self.year = year