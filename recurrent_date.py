"""
This module has the implementation of recurrent dates
"""
import arrow
import json

class RecurrentDate(object):
    """
    Implementation of the yearly repeated dates
    """

    def __init__(self, day, month, description=""):
        self.day = day
        self.month = month
        self.description = description

    def to_dict(self, timezone="Europe/Istanbul") -> str:
        year = arrow.now(timezone).timetuple()[0]
        return {
            'description': self.description,
            'datetime': arrow.Arrow(year, self.month, self.day).for_json()
        }
