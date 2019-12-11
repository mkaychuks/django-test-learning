from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=timezone.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_list')
