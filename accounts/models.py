from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link task to user
    title = models.CharField(max_length=200)  # Task title
    description = models.TextField(blank=True, null=True)  # Optional description
    completed = models.BooleanField(default=False)  # Task status
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return self.title
