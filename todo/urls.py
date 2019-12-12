from django.urls import path


from .views import (
    list_todo, todo_detail,
    create_todo, update_todo,
    delete_todo,
)

urlpatterns = [
    path('todo/', list_todo, name='todo_list'),
    path('todo/<int:pk>/', todo_detail, name='todo_detail'),
    path('todo/new/', create_todo, name='create_todo'),
    path('todo/<int:pk>/edit/', update_todo, name='update_todo'),
    path('todo/<int:pk>/delete/', delete_todo, name='delete_todo'),
]
