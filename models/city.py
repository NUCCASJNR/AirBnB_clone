#!/usr/bin/python3
"""This module inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        city class
    """
    state_id = ""
    name = ""
