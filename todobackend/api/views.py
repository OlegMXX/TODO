from rest_framework import generics
from .serializers import TodoSrializer
from todo.models import Todo


class TodoList(generics.ListAPIView):
    # ListApiView requires teo mandatory attributes, serializer_class and queryset.
    # We specify TodoSerializer which we have earlier implemented
    serializer_class = TodoSrializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')
