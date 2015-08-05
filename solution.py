testing = False

import api
import unittest

class Tank:
    """
    Class for the object that represents the tank that
    is manouvered in the challenge.
    """
    def __init__(self):
        """
        Method that initialises Tank class.
        Placeholder for now.
        """
        pass

class TestTank(unittest.TestCase):
    """
    Unit tests for Tank class.
    Placeholder for now.
    """

class Solution:
    """
    Class given by challenge. Entrence point.
    """
    def __init__(self):
        """
        Method that initialises Solution class.
        Instantiates Tank class.
        If global variable 'testing' is true, runs unit tests.
        """
        if testing:
            unittest.main("solution")
        self.tank = Tank()
    def update(self):
        """
        Method that is run by the server each tick.
        """
        pass
