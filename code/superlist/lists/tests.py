from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):
    def test_haha(self):
        self.assertEqual(2, 3)
