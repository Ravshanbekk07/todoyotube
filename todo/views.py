from django.shortcuts import render

# Create your views here.
from .models import Todo
from .seriaizers import TodoSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView


class ListTodo(ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class ListDetail(RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

