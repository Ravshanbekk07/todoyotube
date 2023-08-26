from .views import ListTodo,ListDetail
from django.urls import path

urlpatterns=[
    path('',ListTodo.as_view()),
    path('<int:pk>/',ListDetail.as_view()),
]