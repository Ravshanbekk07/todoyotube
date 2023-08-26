from .views import ListTodo,ListDetail
from django.urls import path

urlpatterns=[
    path('',ListDetail.as_view()),
    path('<int:pk>',ListTodo.as_view()),
]