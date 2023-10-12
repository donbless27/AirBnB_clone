#!/usr/bin/python3
"""The Review class module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
