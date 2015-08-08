TESTING = False

import api
import random
import unittest
import unittest.mock


class Behaviour:

    """
    Class for handling the tank's behaviour.
    """

    def __init__(self):

        """
        Method that initialises Behaviour class.
        Seeds pseudo random number generator.
        Declares variables current, turning ratio and random limit.
        """

        random.seed(4) # Chosen by fair dice roll, guaranteed to be random ;)

        self.current = 'roaming'
        self.turning_ratio = 1/10
        self.random_limit = 2 * (1/self.turning_ratio)

    def random_turn(self):

        """
        Method that generates a random turn with equal
        probability to the left or to the right.
        """

        direction = random.choice(['left', 'right'])

        if direction == 'left':
            api.turn_left()
            return "Left turn"
        elif direction == 'right':
            api.turn_right()
            return "Right turn"
        else:
            return "No turn"

    def roam(self):

        """
        Method that executes roaming behaviour.
        Decides what to do based on randomness, with the chance
        of turning decided by the turnin ratio from the behaviour
        class.
        """

        random_number = random.randint(0, self.random_limit)

        if random_number == 0:
            api.turn_left()
            return "Left turn."
        elif random_number  == 1:
            api.turn_right()
            return "Right turn."
        else:
            api.move_forward()
            return "Steady as she goes."

    def update(self):

        """
        Method that executes selected behaviour each server tick.
        """

        if self.current == 'roaming':
            self.roam()
            return "Executed roaming method."


@unittest.mock.patch('solution.api')
class testBehaviour(unittest.TestCase):

    """
    Unit tests for Behaviour class.
    Tests method roam.
    """

    @unittest.mock.patch('random.randint', side_effect=[0,1,2])
    def testRoam(self,mock_api,mock_random):

        """
        Unit test for roam method.
        Asserts that random turning is working as it should.
        """

        self.behaviour = Behaviour()
        self.assertEqual(self.behaviour.roam(),'Left turn.')
        self.assertEqual(self.behaviour.roam(),'Right turn.')
        self.assertEqual(self.behaviour.roam(),'Steady as she goes.')

    @unittest.mock.patch('random.choice', side_effect=['left', 'right', 'lol'])
    def testRandom_Turn(self, mock_api, mock_random):

        """
        Unit test for random_turn method.
        Asserts the method executes turns as ordered.
        """

        self.behaviour = Behaviour()
        self.assertEqual(self.behaviour.random_turn(),'Left turn')
        self.assertEqual(self.behaviour.random_turn(),'Right turn')
        self.assertEqual(self.behaviour.random_turn(),'No turn')


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


@unittest.mock.patch('solution.api')
class TestFuel(unittest.TestCase):

    """
    Unit test for Fuel class.
    Tests delta and update methods.
    """

    def testDelta(self,mock_api):

        """
        Unit test that asserts delta method subtraction is... subtracting.
        """

        self.fuel = Fuel()
        self.fuel.old_fuel = 3
        self.fuel.current_fuel = 2
        self.assertEqual(self.fuel.delta(), 1)

    def testUpdate(self,mock_api):

        """
        Unit test that asserts update method is updating variables correctly.
        """

        mock_api.current_fuel.return_value = 1
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
        Instantiates Fuel and Behaviour classes.
        """

        self.fuel = Fuel()
        self.behaviour = Behaviour()

    def damage(self):

        """
        Method that returns bool value, true if damage has been taken since
        last hit, false otherwise.
        """

        consumed_fuel = self.fuel.delta()

        if not consumed_fuel:
            return False
        elif consumed_fuel < 50:
            return False
        else:
            return True

    def update(self):

        """
        Updates everyting associated with the tank each server tick.
        """

        self.fuel.update()
        self.behaviour.update()


@unittest.mock.patch('solution.api')
class TestTank(unittest.TestCase):

    """
    Unit tests for Tank class.
    Tests damage method.
    """

    @unittest.mock.patch('solution.Fuel.delta', side_effect=[None, 5, 55])
    def testDamage(self, mock_api, mock_delta):

        """
        Unit test that asserts damage method is reporting correctly.
        """

        self.tank = Tank()
        self.assertFalse(self.tank.damage())
        self.assertFalse(self.tank.damage())
        self.assertTrue(self.tank.damage())

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
