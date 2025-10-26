from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    srno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)  # Task title
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
