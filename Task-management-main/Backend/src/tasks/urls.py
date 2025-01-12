from django.contrib import admin
from django.urls import path,include
from .views import TaskListApi,RetrieveUpdateDestroyTaskApi,CreateTaskApi

# URL patterns for the Task API views
urlpatterns = [
    path('',TaskListApi.as_view()),
    path('editTask/<int:pk>',RetrieveUpdateDestroyTaskApi.as_view()),
    path('create/',CreateTaskApi.as_view()),
]