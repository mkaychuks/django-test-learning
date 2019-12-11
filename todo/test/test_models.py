from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from todo.models import Todo


class TestModels(TestCase):

    def setUp(self):

        self.timezone = timezone.now()

        self.user = get_user_model().objects.create_user(
            username = 'mkaychuks',
            email = 'admin@admin.com',
            password = 'testing321',
        )

        self.todo = Todo.objects.create(
            title = 'Sweep the house',
            description = 'Sweeping keeps the house neat',
            author = self.user,
            date_created = self.timezone # this keep adding/using the current time when 
                                         # the setUp function is ran
        )

    def test_absolute_url(self):
        self.assertEqual(self.todo.get_absolute_url(), '/todo/')

    def test_string_representation(self):
        self.assertTrue(str(self.todo.title))
        self.assertEqual(str(self.todo.description), 'Sweeping keeps the house neat')

    def test_user_is_created(self):
        self.assertTrue(self.user)

    def test_model_picks_up_data(self):
        self.assertEqual(self.todo.title, str(self.todo.title))
        self.assertNotEqual(self.todo.date_created, self.timezone) # because 'timezone.now()' keeps changing
        self.assertEquals(f'{self.todo.description}', 'Sweeping keeps the house neat')
        