from django.db import models

class Task(models.Model):
    # Task status choices
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]
    # Task priority choices
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    task = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    date = models.DateField() 

    def __str__(self):
        return self.task