from rest_framework import serializers
from .models import Task

# Serializer for the Task model to convert data to and from JSON
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task', 'description', 'priority', 'date', 'status']