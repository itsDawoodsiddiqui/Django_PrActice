from django.test import TestCase

class FirstTestCase(TestCase):

    # The setUp method is called before each test
    def setUp(self):
        print('setup called')
    
    # This is a test method, it will run and check if the assertion is true
    def test_equal(self):
        self.assertEqual(1, 1)
    
    # Another example: testing for inequality
    def test_not_equal(self):
        self.assertNotEqual(1, 2)
    
    # Testing for truth
    def test_truth(self):
        self.assertTrue(True)
    
    # Testing for falsehood
    def test_false(self):
        self.assertFalse(False)
