from django.test import TestCase

class MyTestCase(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_nothing(self):
        self.assertTrue(True)
