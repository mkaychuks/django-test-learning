from django.urls import path


from .views import list_todo, todo_detail

urlpatterns = [
    path('todo/', list_todo, name='todo_list'),
    path('todo/<int:pk>/', todo_detail, name='todo_detail'),
]