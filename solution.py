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
    def delta(self):
        """
        Method that returns the fuel difference since last server tick.
        """
        if self.old_fuel and self.current_fuel:
            return self.old_fuel - self.current_fuel
        else:
            return None
    def update(self):
        """
        Method that updates the fuel levels each tick.
        """
        self.old_fuel = self.current_fuel
        self.current_fuel = api.current_fuel()

class TestFuel(unittest.TestCase):
    """
    Unit test for Fuel class.
    Tests delta method.
    """
    def testDelta(self):
        """
        Unit test that asserts delta method subtraction is... subtracting.
        """
        self.fuel = Fuel()
        self.fuel.old_fuel = 3
        self.fuel.current_fuel = 2
        self.assertEqual(self.fuel.delta(), 1)

class Tank:
    """
    Class for the object that represents the tank that
    is manouvered in the challenge.
    """
    def __init__(self):
        """
        Method that initialises Tank class.
        Instantiates Fuel class.
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
        self.tank.update()
