testing = False

import api
import unittest

class Fuel:
    """
    Class for handling calculations related to the tank's fuel.
    """
    def __init__(self):
        """
        Method that initialises Fuel class.
        Declares variables old_fuel and current_fuel.
        """
        self.old_fuel = None
        self.current_fuel = None
    def update(self):
        """
        Method that updates the fuel levels each tick.
        """
        self.old_fuel = self.current_fuel
        self.current_fuel = api.current_fuel()

class testFuel(unittest.TestCase):
    """
    Unit test for Fuel class.
    Placeholder for now.
    """

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
        self.fuel = Fuel()
    def update(self):
        """
        Updates everyting associated with the tank each server tick.
        """
        self.fuel.update()

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
        print(self.tank.fuel.current_fuel)
        self.tank.update()
