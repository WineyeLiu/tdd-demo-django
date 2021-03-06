from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
from lists.models import Item

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
    '''
    def test_return_html(self):
        request = HttpRequest()
        response = home_page(request)
        html_text = render_to_string('home.html')
        self.assertEqual(response.content.decode(), html_text)
    '''
    def test_home_page_return_correct_html(self):
        pass

    def test_home_page_can_save_a_Post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        # self.assertIn('A new list item', response.content.decode())

    def test_home_page_only_save_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_home_page_displays_all_list_items(self):
        Item.objects.create(text='itemey1')
        Item.objects.create(text='itemey2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('itemey1', response.content.decode())
        self.assertIn('itemey2', response.content.decode())

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'the first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'the first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

class ListViewTest(TestCase):

    def test_displays_all_items(self):
        Item.objects.create(text='itemey1')
        Item.objects.create(text='itemey2')

        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertContains(response, 'itemey1')
        self.assertContains(response, 'itemey2')
