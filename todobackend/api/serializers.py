from rest_framework import serializers
from todo.models import Todo


class TodoSrializer(serializers.ModelSerializer):
    # auto populated by app, user can't manipulate
    # uses when there is (default=Bool) in a model
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'completed']


class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title', 'memo', 'created', 'completed']
