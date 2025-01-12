from rest_framework.generics import *
from .models import Task
from .serializers import TaskSerializer

# API view to list all tasks
class TaskListApi(ListAPIView):
    queryset = Task.objects.all()
    serializer_class =  TaskSerializer

# API view to create a new task    
class CreateTaskApi(CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

# API view to retrieve, update or delete a task
class RetrieveUpdateDestroyTaskApi(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class =  TaskSerializer