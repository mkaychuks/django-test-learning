from django.test import TestCase
from django.contrib.auth import get_user_model

from todo.forms import TodoForm


class TestTodo(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username = 'mkaychuks',
                email = 'admin@admin.com',
                password = 'testing321',
            )

    def test_form_is_valid(self):
        response = TodoForm({
            'title': 'Welcome to Universe',
            'description': 'Yahoo yahoo this universe',
            'author': self.user
        })
        self.assertTrue(response.is_valid)

    def test_form_is_invalid(self):
        response = TodoForm({

        })
        self.assertTrue(response.has_error)
        self.assertFalse(response._errors)