"""
api - containing functions that we all love
"""

from datetime import datetime
from time import strftime
import random

__version__ = "0.1.0"

def get_today():
    """
    Return today's date

    :return: today's date
    :rtype: str
    """
    return datetime.now().strftime('%d%m%Y')

def get_random_number():
    """
    Return a random number bewteen 0 - 100

    :return: a random number bewteen 0 - 100
    :rtype: int
    """
    return random.randint(0, 100)
