from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone


from todo.models import Todo


class TestViews(TestCase):

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
            date_created = self.timezone  # this keep adding/using the current
                                          # time when the setUp function is ran
        )

    def test_list_todo_view(self):
        response = self.client.get(reverse('todo_list'))
        no_response = self.client.get('todos')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'index.html')

    def test_todo_detail_view(self):
        response = self.client.get(reverse('todo_detail', args='1'))
        no_response = self.client.get(reverse('todo_detail', args='2'))
        self.assertTemplateUsed(response, 'detail.html')
        self.assertEquals(no_response.status_code, 404)
        self.assertContains(response, 'Sweep the house')

    def test_create_todo_view(self):
        response = self.client.post('/todo/new/', {
            'title': 'Welcome to a wonderful world',
            'description': 'About to understand the meaning of things',
            'author': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'About to understand the meaning of things'
        )
        self.assertTemplateUsed(response, 'form.html')

    def test_update_todo_view(self):
        response = self.client.post('/todo/1/edit/', {
            'title': 'Welcome',
            'description': 'About to understand the meaning',
            'author': self.user
        })
        self.assertTemplateUsed(response, 'update.html')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, self.user)

    def test_delete_todo_view(self):
        response = self.client.get(reverse('delete_todo', args='1'))
        if response.status_code != 200:
            self.assertEquals(response.status_code, 302)
