from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.
'''
class SmokeTest(TestCase):
    def test_haha(self):
        self.assertEqual(2, 3)

'''
class HomePageTest(TestCase):
    def test_root_url_resolve(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page) 
    
    def test_return_html(self):
        request = HttpRequest()
        response = home_page()
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
