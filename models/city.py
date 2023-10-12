#!/usr/bin/python3
"""City class module"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class for managing city objects"""

    state_id = ""
    name = ""
