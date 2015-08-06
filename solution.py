TESTING = False

import api
import unittest
import unittest.mock


class Behaviour:

    """
    Class for handling the tank's behaviour.
    """

    def __init__(self):

        """
        Method that initialises Behaviour class.
        Declares variable current.
        """

        self.current = 'roaming'

    def roam(self):

        """
        Method that executes roaming behaviour.
        Placeholder for now.
        """

        pass


class testBehaviour(unittest.TestCase):

    """
    Unit tests for Behaviour class.
    Placeholder for now.
    """

    def testRoam(self):

        """
        Unit test for roam method.
        Placeholder for now.
        """

        pass
        

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
    Tests delta and update methods.
    """

    def testDelta(self):

        """
        Unit test that asserts delta method subtraction is... subtracting.
        """

        self.fuel = Fuel()
        self.fuel.old_fuel = 3
        self.fuel.current_fuel = 2
        self.assertEqual(self.fuel.delta(), 1)

    def testUpdate(self):

        """
        Unit test that asserts update method is updating variables correctly.
        """

        mock = unittest.mock.MagicMock(return_value = 1)
        with unittest.mock.patch('api.current_fuel', mock):
            self.fuel = Fuel()
            self.fuel.current_fuel = 2
            self.fuel.old_fuel = 3
            self.fuel.update()
            self.assertEqual(self.fuel.old_fuel, 2)
            self.assertEqual(self.fuel.current_fuel, 1)


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

    def damage(self):

        """
        Method that returns bool value, true if damage has been taken since
        last hit, false otherwise.
        """

        if not self.fuel.delta():
            return False
        elif self.fuel.delta() < 50:
            return False
        else:
            return True

    def update(self):

        """
        Updates everyting associated with the tank each server tick.
        """

        self.fuel.update()


class TestTank(unittest.TestCase):

    """
    Unit tests for Tank class.
    Tests damage method.
    """

    def testDamage(self):

        """
        Unit test that asserts damage method is reporting correctly.
        """

        mock = unittest.mock.MagicMock(return_value = 5)
        with unittest.mock.patch('solution.Fuel.delta', mock):
            self.tank = Tank()
            self.assertFalse(self.tank.damage())

        mock = unittest.mock.MagicMock(return_value = 55)
        with unittest.mock.patch('solution.Fuel.delta', mock):
            self.tank = Tank()
            self.assertTrue(self.tank.damage())

        mock = unittest.mock.MagicMock(return_value = None)
        with unittest.mock.patch('solution.Fuel.delta', mock):
            self.tank = Tank()
            self.assertFalse(self.tank.damage())


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

        if TESTING:
            unittest.main("solution")

        self.tank = Tank()

    def update(self):

        """
        Method that is run by the server each tick.
        """

        self.tank.update()
