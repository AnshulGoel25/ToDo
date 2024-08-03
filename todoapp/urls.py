from django.urls import path
from .views import *

urlpatterns = [
    path('create-category', CategoryCreateView.as_view(), name="create_category"),
    path('create-task', TodoCreateView.as_view(), name="create_todo"),
    path('tasks', TodoListView.as_view(), name="todo_list"),
    path('categories', CategoryListView.as_view(), name="category_list"),
]
