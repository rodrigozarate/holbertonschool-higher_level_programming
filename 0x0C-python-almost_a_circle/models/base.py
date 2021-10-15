#!/usr/bin/python3
""" Module base clase """


class Base:
__nb_objects = 0
def __init__(self, id=None):
if id is not None:
id = self.id
else
__nb_objects +=1
id = __nb_objects
