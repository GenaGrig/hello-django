from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # Create a form with a blank name field
        form = ItemForm({'name': ''})
        # Check that the form is not valid
        self.assertFalse(form.is_valid())
        # Check that the name field has the correct error
        self.assertIn('name', form.errors.keys())
        # Check that the error is the expected one
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # Create a form with a blank name field
        form = ItemForm({'name': 'Test Todo Item'})
        # Check that the form is valid
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # Create a form with a blank name field
        form = ItemForm()
        # Check that the form has specified the expected fields
        self.assertEqual(form.Meta.fields, ['name', 'done'])
        