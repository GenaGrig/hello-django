from django.test import TestCase
from .models import Item


# Create your tests here.
class TestViews(TestCase):
    def test_get_todo_list(self):
        # Issue a GET request to the add_item view
        response = self.client.get('/')
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check the correct template is used
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        # Issue a GET request to the add_item view
        response = self.client.get('/add')
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check the correct template is used
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # Create an item to edit
        item = Item.objects.create(name='Test Todo Item')
        # Issue a GET request to the edit_item view
        response = self.client.get(f'/edit/{item.id}')
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check the correct template is used
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # Issue a POST request to the add_item view
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # Check that the response is 302 FOUND
        self.assertEqual(response.status_code, 302)
        # Check that the item was added to the database
        item = Item.objects.get(id=1)
        self.assertEqual(item.name, 'Test Added Item')
        # Check that the item is not done
        self.assertFalse(item.done)

    def test_can_delete_item(self):
        # Create an item to delete
        item = Item.objects.create(name='Test Todo Item')
        # Issue a GET request to the delete_item view
        response = self.client.get(f'/delete/{item.id}')
        # Check that the response is 302 FOUND
        self.assertEqual(response.status_code, 302)
        # Check that the item was deleted from the database
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # Create an item to toggle
        item = Item.objects.create(name='Test Todo Item', done=True)
        # Issue a GET request to the toggle_item view
        response = self.client.get(f'/toggle/{item.id}')
        # Check that the response is 302 FOUND
        self.assertEqual(response.status_code, 302)
        # Check that the item's done field is updated
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
        
    def test_can_edit_item(self):
        # Create an item to edit
        item = Item.objects.create(name='Test Todo Item')
        # Issue a POST request to the edit_item view
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        # Check that the response is 302 FOUND
        self.assertEqual(response.status_code, 302)
        # Check that the item's name is updated
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
        
    def test_can_redirect_after_POST(self):
        # Issue a POST request to the add_item view
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # Check that the response is 302 FOUND
        self.assertEqual(response.status_code, 302)
        # Check that the response redirects to the correct page
        self.assertRedirects(response, '/')