testing = False

import api
import unittest

class Solution:
    """
    Class given by challenge. Entrence point.
    """
    def __init__(self):
        """
        Method that initialises Solution class.
        If global variable 'testing' is true, runs unit tests.
        """
        if testing:
            unittest.main("solution")

    def update(self):
        """
        Method that is run by the server each tick.
        """
        pass
