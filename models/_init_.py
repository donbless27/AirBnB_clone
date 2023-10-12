#!/usr/bin/python3
"""_init_ magic method that initializes the package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
