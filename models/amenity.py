#!/usr/bin/python3
"""Module that defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
