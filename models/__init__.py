#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import environ as env

if env.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
