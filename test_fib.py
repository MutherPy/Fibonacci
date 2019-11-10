import unittest
import fibonacci as fib

class FibonTest(unittest.TestCase):
    """ Fibonacci numbers test """
        
    @classmethod
    def setUpClass(cls):
        """ Set up for class """
        print('\n Fibonacci test start: ')
        print(' +++++++++++++ ')
        
    @classmethod
    def tearDownClass(cls):
        """ Tear down for class """
        print(' ------------- ')
        print(' Fibonacci test end ')
        
    def setUp(self):
        """ For comfort """
        print(' --> ')


    def test_argument_string(self):
        """ Current arg is string. TypeError """
        self.assertRaises(TypeError, fib.fibon, 'privet')

    def test_argument_list(self):
        """ Current arg is list. TypeError  """
        self.assertRaises(TypeError, fib.fibon, [5])

    def test_argument_set(self):
        """ Current arg is set. TypeError  """
        self.assertRaises(TypeError, fib.fibon, {5})

    def test_argument_dict(self):
        """ Current arg is dict. TypeError  """
        self.assertRaises(TypeError, fib.fibon, {'a':5})

    def test_argument_negative(self):
        """ Current arg is negative. RecursionError """
        self.assertRaises(RecursionError, fib.fibon, -3)

    def test_return_amount(self):
        """ Correct return length """
        self.assertEqual(len(fib.fibon(10)), 10)

    def test_not_none(self):
        """ Is return not None """
        self.assertIsNotNone(fib.fibon(10))
        
    def test_fibon_equal(self):
        """ Is return value is equal with example """
        self.assertEqual(fib.fibon(10),[1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


if __name__ == '__main__':
    unittest.main()
